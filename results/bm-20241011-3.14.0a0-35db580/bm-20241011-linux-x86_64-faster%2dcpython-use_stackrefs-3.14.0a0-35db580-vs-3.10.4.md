# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 35db580
- commit date: 2024-10-11
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.35x faster                                                     |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                   |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                    |
| tornado_http   | 136 ms                                                 | 92.5 ms: 1.47x faster                                                    |
| Geometric mean | (ref)                                                  | 1.37x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 334 ms: 2.18x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 427 ms: 2.04x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 960 ms: 1.84x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 578 ms: 1.76x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.95x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.2 ms: 1.65x faster                                                    |
| float          | 117 ms                                                 | 79.4 ms: 1.47x faster                                                    |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                     |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.15x faster                                                    |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.15x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                    |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 86.6 ms: 1.15x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                                     |
| unpickle             | 14.4 us                                                | 15.4 us: 1.07x slower                                                    |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                    |
| pickle_dict          | 29.6 us                                                | 34.1 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                             |

Benchmark hidden because not significant (2): pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 22.5 ms: 1.42x faster                                                    |
| mako            | 16.3 ms                                                | 11.8 ms: 1.38x faster                                                    |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                     |
| generators               | 80.1 ms                                                | 29.2 ms: 2.74x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                                    |
| async_tree_none          | 728 ms                                                 | 334 ms: 2.18x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 427 ms: 2.04x faster                                                     |
| go                       | 240 ms                                                 | 121 ms: 1.99x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 483 ms: 1.91x faster                                                     |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 31.2 us: 1.87x faster                                                    |
| chaos                    | 115 ms                                                 | 62.1 ms: 1.86x faster                                                    |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 960 ms: 1.84x faster                                                     |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 578 ms: 1.76x faster                                                     |
| richards_super           | 94.7 ms                                                | 54.0 ms: 1.76x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 69.0 ms: 1.71x faster                                                    |
| pylint                   | 551 ms                                                 | 325 ms: 1.70x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                                    |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                    |
| richards                 | 79.3 ms                                                | 47.3 ms: 1.68x faster                                                    |
| nbody                    | 154 ms                                                 | 93.2 ms: 1.65x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.32 ms: 1.64x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                    |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                    |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                   |
| tornado_http             | 136 ms                                                 | 92.5 ms: 1.47x faster                                                    |
| float                    | 117 ms                                                 | 79.4 ms: 1.47x faster                                                    |
| pyflate                  | 716 ms                                                 | 490 ms: 1.46x faster                                                     |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.80 us: 1.43x faster                                                    |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                    |
| logging_format           | 9.09 us                                                | 6.40 us: 1.42x faster                                                    |
| genshi_text              | 31.8 ms                                                | 22.5 ms: 1.42x faster                                                    |
| coroutines               | 35.1 ms                                                | 25.3 ms: 1.39x faster                                                    |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.38x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.70 ms: 1.38x faster                                                    |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                    |
| 2to3                     | 348 ms                                                 | 259 ms: 1.35x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                   |
| thrift                   | 1.07 ms                                                | 802 us: 1.34x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 763 ms: 1.33x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.32x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                     |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.31x faster                                                     |
| nqueens                  | 106 ms                                                 | 82.0 ms: 1.29x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 65.4 ms: 1.29x faster                                                    |
| scimark_fft              | 466 ms                                                 | 361 ms: 1.29x faster                                                     |
| unpack_sequence          | 60.0 ns                                                | 46.6 ns: 1.29x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                    |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 54.9 ms: 1.26x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                    |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                    |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                     |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 858 us: 1.15x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 86.6 ms: 1.15x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.15x faster                                                    |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                    |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                    |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                    |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                     |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                                    |
| coverage                 | 79.4 ms                                                | 84.7 ms: 1.07x slower                                                    |
| unpickle                 | 14.4 us                                                | 15.4 us: 1.07x slower                                                    |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                    |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                    |
| pickle_dict              | 29.6 us                                                | 34.1 us: 1.15x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 56.2 ms: 2.34x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                             |

Benchmark hidden because not significant (3): pickle_list, async_generators, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241011-3.14.0a0-35db580/bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.12x
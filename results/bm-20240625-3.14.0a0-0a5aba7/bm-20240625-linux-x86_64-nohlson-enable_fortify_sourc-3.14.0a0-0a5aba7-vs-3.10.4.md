# Results vs. 3.10.4

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 0a5aba7
- commit date: 2024-06-25
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.31x faster                                                   |
| docutils       | 3.30 sec                                               | 2.74 sec: 1.20x faster                                                 |
| html5lib       | 88.9 ms                                                | 66.8 ms: 1.33x faster                                                  |
| tornado_http   | 136 ms                                                 | 96.2 ms: 1.42x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 412 ms: 2.11x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 840 ms: 2.11x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.4 ms: 1.80x faster                                                  |
| float          | 117 ms                                                 | 77.0 ms: 1.52x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.41x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                  |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                  |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.07x faster                                                   |
| unpickle_list        | 5.20 us                                                | 5.27 us: 1.01x slower                                                  |
| unpickle             | 14.4 us                                                | 14.9 us: 1.03x slower                                                  |
| pickle               | 10.7 us                                                | 11.9 us: 1.11x slower                                                  |
| pickle_dict          | 29.6 us                                                | 34.6 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.48x faster                                                  |
| django_template | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.8 ms: 1.30x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                   |
| generators               | 80.1 ms                                                | 29.1 ms: 2.75x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                  |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 412 ms: 2.11x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 840 ms: 2.11x faster                                                   |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 482 ms: 1.91x faster                                                   |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                                   |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                   |
| nbody                    | 154 ms                                                 | 85.4 ms: 1.80x faster                                                  |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                                  |
| pylint                   | 551 ms                                                 | 314 ms: 1.76x faster                                                   |
| richards_super           | 94.7 ms                                                | 54.2 ms: 1.75x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.10 ms: 1.70x faster                                                  |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                                  |
| richards                 | 79.3 ms                                                | 48.4 ms: 1.64x faster                                                  |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                  |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.55x faster                                                   |
| float                    | 117 ms                                                 | 77.0 ms: 1.52x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                   |
| pyflate                  | 716 ms                                                 | 479 ms: 1.49x faster                                                   |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.48x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                 |
| tornado_http             | 136 ms                                                 | 96.2 ms: 1.42x faster                                                  |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                   |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| nqueens                  | 106 ms                                                 | 79.1 ms: 1.34x faster                                                  |
| thrift                   | 1.07 ms                                                | 805 us: 1.33x faster                                                   |
| html5lib                 | 88.9 ms                                                | 66.8 ms: 1.33x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                   |
| 2to3                     | 348 ms                                                 | 267 ms: 1.31x faster                                                   |
| scimark_fft              | 466 ms                                                 | 357 ms: 1.30x faster                                                   |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.8 ms: 1.30x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.06 ms: 1.28x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 54.5 ms: 1.27x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                  |
| sympy_sum                | 196 ms                                                 | 158 ms: 1.24x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 804 us: 1.23x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 68.8 ms: 1.23x faster                                                  |
| sympy_str                | 346 ms                                                 | 282 ms: 1.22x faster                                                   |
| dask                     | 441 ms                                                 | 360 ms: 1.22x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.74 sec: 1.20x faster                                                 |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                  |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                   |
| json                     | 5.69 ms                                                | 5.15 ms: 1.10x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.07x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                 |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 3.54 ms: 1.02x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.96 us: 1.02x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| async_generators         | 444 ms                                                 | 437 ms: 1.01x faster                                                   |
| unpickle_list            | 5.20 us                                                | 5.27 us: 1.01x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                  |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.03x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                  |
| pickle                   | 10.7 us                                                | 11.9 us: 1.11x slower                                                  |
| telco                    | 7.27 ms                                                | 8.31 ms: 1.14x slower                                                  |
| coverage                 | 79.4 ms                                                | 91.3 ms: 1.15x slower                                                  |
| pickle_dict              | 29.6 us                                                | 34.6 us: 1.17x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240625-3.14.0a0-0a5aba7/bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.11x
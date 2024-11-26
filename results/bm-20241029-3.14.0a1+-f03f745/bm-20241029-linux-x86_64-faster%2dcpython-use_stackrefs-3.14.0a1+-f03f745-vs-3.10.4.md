# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.385x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                      |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.21x faster                                                    |
| html5lib       | 88.9 ms                                                | 64.1 ms: 1.39x faster                                                     |
| tornado_http   | 136 ms                                                 | 92.5 ms: 1.47x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 334 ms: 2.18x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 422 ms: 2.06x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 882 ms: 2.00x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 583 ms: 1.74x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.3 ms: 1.63x faster                                                     |
| float          | 117 ms                                                 | 81.1 ms: 1.44x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.44x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                     |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 60.6 ms: 1.31x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| json_loads           | 31.2 us                                                | 26.5 us: 1.18x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 87.4 ms: 1.14x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                     |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                     |
| django_template | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                      |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.31 ms: 2.39x faster                                                     |
| async_tree_none          | 728 ms                                                 | 334 ms: 2.18x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 422 ms: 2.06x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 882 ms: 2.00x faster                                                      |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.90x faster                                                     |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                      |
| chaos                    | 115 ms                                                 | 62.5 ms: 1.85x faster                                                     |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                      |
| richards_super           | 94.7 ms                                                | 52.5 ms: 1.80x faster                                                     |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 73.3 ms: 1.74x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 583 ms: 1.74x faster                                                      |
| richards                 | 79.3 ms                                                | 46.2 ms: 1.71x faster                                                     |
| pylint                   | 551 ms                                                 | 322 ms: 1.71x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 69.5 ms: 1.70x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                     |
| scimark_sor              | 220 ms                                                 | 135 ms: 1.63x faster                                                      |
| nbody                    | 154 ms                                                 | 94.3 ms: 1.63x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.60x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                      |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                    |
| pyflate                  | 716 ms                                                 | 482 ms: 1.49x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.81 us: 1.48x faster                                                     |
| tornado_http             | 136 ms                                                 | 92.5 ms: 1.47x faster                                                     |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.47x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                     |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                                     |
| regex_compile            | 188 ms                                                 | 130 ms: 1.44x faster                                                      |
| float                    | 117 ms                                                 | 81.1 ms: 1.44x faster                                                     |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                     |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                     |
| html5lib                 | 88.9 ms                                                | 64.1 ms: 1.39x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                    |
| django_template          | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                     |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                    |
| thrift                   | 1.07 ms                                                | 803 us: 1.33x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 763 ms: 1.33x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 64.5 ms: 1.31x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 60.6 ms: 1.31x faster                                                     |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.31x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                      |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.09 ms: 1.27x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.27x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 54.7 ms: 1.26x faster                                                     |
| scimark_fft              | 466 ms                                                 | 370 ms: 1.26x faster                                                      |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                      |
| fannkuch                 | 532 ms                                                 | 427 ms: 1.25x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.21x faster                                                    |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                      |
| json_loads               | 31.2 us                                                | 26.5 us: 1.18x faster                                                     |
| json                     | 5.69 ms                                                | 4.89 ms: 1.16x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 858 us: 1.15x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 87.4 ms: 1.14x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.13x faster                                                    |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                      |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| async_generators         | 444 ms                                                 | 439 ms: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                     |
| coverage                 | 79.4 ms                                                | 83.9 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 7.96 ms: 1.09x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.55 ms: 1.26x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 79.1 ms: 3.29x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                              |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241029-3.14.0a1+-f03f745/bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.385x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.25x
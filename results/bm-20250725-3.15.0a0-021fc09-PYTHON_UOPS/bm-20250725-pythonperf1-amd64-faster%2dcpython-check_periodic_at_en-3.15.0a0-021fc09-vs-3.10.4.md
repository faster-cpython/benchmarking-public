# Results vs. 3.10.4

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: windows-amd64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.156x faster
- HPT reliability: 99.77%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 250 ms: 1.02x slower                                                                 |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                               |
| html5lib       | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                                |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 438 ms: 2.53x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 223 ms: 2.36x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 192 ms: 2.26x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 350 ms: 1.82x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.23x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.7 ms: 1.35x faster                                                                |
| nbody          | 71.3 ms                                                     | 87.0 ms: 1.22x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 95.1 ms: 1.12x faster                                                                |
| regex_dna      | 136 ms                                                      | 125 ms: 1.09x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                                |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 249 us: 1.08x faster                                                                 |
| xml_etree_parse      | 96.8 ms                                                     | 91.4 ms: 1.06x faster                                                                |
| tomli_loads          | 1.67 sec                                                    | 1.70 sec: 1.02x slower                                                               |
| xml_etree_process    | 44.5 ms                                                     | 45.6 ms: 1.03x slower                                                                |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 70.5 ms: 1.09x slower                                                                |
| unpickle_pure_python | 183 us                                                      | 209 us: 1.14x slower                                                                 |
| xml_etree_generate   | 55.5 ms                                                     | 65.1 ms: 1.17x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.31x slower                                                                |
| python_startup         | 20.6 ms                                                     | 27.4 ms: 1.33x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                                |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                                |
| mako            | 9.03 ms                                                     | 8.86 ms: 1.02x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 124 us: 2.71x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 438 ms: 2.53x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 223 ms: 2.36x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 33.4 ms: 2.27x faster                                                                |
| async_tree_none          | 435 ms                                                      | 192 ms: 2.26x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 862 ms: 2.06x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 350 ms: 1.82x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                                |
| go                       | 139 ms                                                      | 83.6 ms: 1.66x faster                                                                |
| pylint                   | 350 ms                                                      | 212 ms: 1.65x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 58.6 ns: 1.62x faster                                                                |
| richards_super           | 52.2 ms                                                     | 32.5 ms: 1.61x faster                                                                |
| generators               | 32.4 ms                                                     | 20.3 ms: 1.59x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.53x faster                                                                |
| richards                 | 42.4 ms                                                     | 28.7 ms: 1.48x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                                |
| raytrace                 | 273 ms                                                      | 193 ms: 1.41x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 61.3 ms: 1.40x faster                                                                |
| deepcopy                 | 255 us                                                      | 183 us: 1.39x faster                                                                 |
| float                    | 61.7 ms                                                     | 45.7 ms: 1.35x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.6 ms: 1.34x faster                                                                |
| scimark_sor              | 106 ms                                                      | 79.1 ms: 1.34x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.60 ms: 1.25x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                                |
| thrift                   | 617 us                                                      | 508 us: 1.21x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                                |
| pyflate                  | 409 ms                                                      | 338 ms: 1.21x faster                                                                 |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 65.6 ms: 1.18x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                                |
| sympy_sum                | 107 ms                                                      | 94.4 ms: 1.13x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 44.7 ms: 1.13x faster                                                                |
| regex_compile            | 106 ms                                                      | 95.1 ms: 1.12x faster                                                                |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                                |
| pycparser                | 930 ms                                                      | 853 ms: 1.09x faster                                                                 |
| regex_dna                | 136 ms                                                      | 125 ms: 1.09x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                                |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                               |
| pickle_pure_python       | 270 us                                                      | 249 us: 1.08x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 91.4 ms: 1.06x faster                                                                |
| sympy_str                | 194 ms                                                      | 185 ms: 1.05x faster                                                                 |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                                |
| mako                     | 9.03 ms                                                     | 8.86 ms: 1.02x faster                                                                |
| 2to3                     | 246 ms                                                      | 250 ms: 1.02x slower                                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.70 sec: 1.02x slower                                                               |
| xml_etree_process        | 44.5 ms                                                     | 45.6 ms: 1.03x slower                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.25 sec: 1.03x slower                                                               |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 64.6 ms: 1.03x slower                                                                |
| logging_simple           | 6.22 us                                                     | 6.44 us: 1.03x slower                                                                |
| sympy_expand             | 314 ms                                                      | 326 ms: 1.04x slower                                                                 |
| logging_format           | 6.76 us                                                     | 7.02 us: 1.04x slower                                                                |
| nqueens                  | 66.6 ms                                                     | 70.6 ms: 1.06x slower                                                                |
| pprint_safe_repr         | 592 ms                                                      | 632 ms: 1.07x slower                                                                 |
| xml_etree_iterparse      | 65.0 ms                                                     | 70.5 ms: 1.09x slower                                                                |
| meteor_contest           | 75.9 ms                                                     | 86.2 ms: 1.14x slower                                                                |
| unpickle_pure_python     | 183 us                                                      | 209 us: 1.14x slower                                                                 |
| async_generators         | 222 ms                                                      | 259 ms: 1.17x slower                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 65.1 ms: 1.17x slower                                                                |
| scimark_fft              | 187 ms                                                      | 221 ms: 1.18x slower                                                                 |
| nbody                    | 71.3 ms                                                     | 87.0 ms: 1.22x slower                                                                |
| telco                    | 3.94 ms                                                     | 5.01 ms: 1.27x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.31x slower                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.58 ms: 1.31x slower                                                                |
| python_startup           | 20.6 ms                                                     | 27.4 ms: 1.33x slower                                                                |
| coverage                 | 39.0 ms                                                     | 53.0 ms: 1.36x slower                                                                |
| fannkuch                 | 256 ms                                                      | 354 ms: 1.38x slower                                                                 |
| gc_traversal             | 1.41 ms                                                     | 2.19 ms: 1.55x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.71x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                                         |

Benchmark hidden because not significant (2): comprehensions, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS/bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.156x faster

# HPT report

- Reliability score: 99.77% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
# Results vs. 3.10.4

- fork: brandtbucher
- ref: msvc_musttail
- machine: windows-amd64
- commit hash: 06bc3bd
- commit date: 2025-03-07
- overall geometric mean: 1.219x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 426 ms: 2.60x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 225 ms: 2.34x faster                                                       |
| async_tree_none         | 435 ms                                                      | 187 ms: 2.33x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 343 ms: 1.86x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.8 ms: 1.38x faster                                                      |
| nbody          | 71.3 ms                                                     | 67.9 ms: 1.05x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.2 ms: 1.22x faster                                                      |
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.86 ms: 1.34x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 230 us: 1.17x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 39.9 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.4 ms: 1.13x faster                                                      |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.12x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 426 ms: 2.60x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.9 ms: 2.37x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 225 ms: 2.34x faster                                                       |
| async_tree_none          | 435 ms                                                      | 187 ms: 2.33x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 343 ms: 1.86x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.30 ms: 1.82x faster                                                      |
| pylint                   | 350 ms                                                      | 207 ms: 1.70x faster                                                       |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                                      |
| go                       | 139 ms                                                      | 86.6 ms: 1.61x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 59.0 ns: 1.60x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.1 ms: 1.50x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 19.9 us: 1.44x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.43x faster                                                      |
| raytrace                 | 273 ms                                                      | 193 ms: 1.41x faster                                                       |
| deepcopy                 | 255 us                                                      | 183 us: 1.39x faster                                                       |
| float                    | 61.7 ms                                                     | 44.8 ms: 1.38x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.28 ms: 1.34x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 64.1 ms: 1.34x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.86 ms: 1.34x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 57.8 ms: 1.34x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                      |
| pyflate                  | 409 ms                                                      | 312 ms: 1.31x faster                                                       |
| richards_super           | 52.2 ms                                                     | 40.6 ms: 1.29x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.1 ms: 1.27x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.2 ms: 1.27x faster                                                      |
| scimark_sor              | 106 ms                                                      | 84.2 ms: 1.26x faster                                                      |
| pycparser                | 930 ms                                                      | 746 ms: 1.25x faster                                                       |
| thrift                   | 617 us                                                      | 504 us: 1.23x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                       |
| regex_compile            | 106 ms                                                      | 87.2 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| richards                 | 42.4 ms                                                     | 35.6 ms: 1.19x faster                                                      |
| sympy_sum                | 107 ms                                                      | 90.0 ms: 1.19x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.8 ms: 1.18x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 230 us: 1.17x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 847 us: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.4 ms: 1.13x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.08 sec: 1.13x faster                                                     |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                     |
| mdp                      | 1.78 sec                                                    | 1.59 sec: 1.12x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 39.9 ms: 1.11x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 533 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 176 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.1 ms: 1.06x faster                                                      |
| sympy_expand             | 314 ms                                                      | 299 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                                      |
| nbody                    | 71.3 ms                                                     | 67.9 ms: 1.05x faster                                                      |
| scimark_fft              | 187 ms                                                      | 180 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.66 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 76.9 ms: 1.01x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.88 us: 1.02x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.41 us: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.08x slower                                                      |
| fannkuch                 | 256 ms                                                      | 282 ms: 1.10x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.78 ms: 1.21x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.1 ms: 1.26x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 87.8 ms: 1.41x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.04 ms: 1.45x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                               |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250307-3.14.0a5+-06bc3bd/bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.219x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown
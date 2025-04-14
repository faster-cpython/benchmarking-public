# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.231x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                       |
| nbody          | 71.3 ms                                                     | 69.1 ms: 1.03x faster                                                       |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 84.1 ms: 1.26x faster                                                       |
| regex_dna      | 136 ms                                                      | 112 ms: 1.22x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.67 ms: 1.37x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 142 us: 1.29x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.6 ms: 1.12x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.40 us: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.84 us: 1.04x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 17.9 us: 1.04x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.96 us: 1.08x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.2 us: 1.08x slower                                                       |
| pickle               | 6.85 us                                                     | 7.87 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                       |
| python_startup         | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.69 ms: 1.35x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                       |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.17x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.15 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 57.2 ns: 1.65x faster                                                       |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                       |
| go                       | 139 ms                                                      | 85.4 ms: 1.63x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.9 ms: 1.59x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.4 us: 1.49x faster                                                       |
| richards                 | 42.4 ms                                                     | 28.7 ms: 1.48x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.9 ms: 1.47x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.46x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.43x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.7 ms: 1.41x faster                                                       |
| deepcopy                 | 255 us                                                      | 183 us: 1.39x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 875 us: 1.39x faster                                                        |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.37x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.67 ms: 1.37x faster                                                       |
| float                    | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.23 ms: 1.36x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 539 ms: 1.36x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.69 ms: 1.35x faster                                                       |
| pyflate                  | 409 ms                                                      | 303 ms: 1.35x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 58.2 ms: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.3 ms: 1.29x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 142 us: 1.29x faster                                                        |
| pycparser                | 930 ms                                                      | 725 ms: 1.28x faster                                                        |
| regex_compile            | 106 ms                                                      | 84.1 ms: 1.26x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                                        |
| scimark_sor              | 106 ms                                                      | 85.4 ms: 1.24x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                      |
| regex_dna                | 136 ms                                                      | 112 ms: 1.22x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 62.4 ms: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                       |
| thrift                   | 617 us                                                      | 515 us: 1.20x faster                                                        |
| sympy_sum                | 107 ms                                                      | 89.4 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.2 ms: 1.20x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.17x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.67 us: 1.14x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.2 ms: 1.13x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 527 ms: 1.12x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 39.6 ms: 1.12x faster                                                       |
| sympy_str                | 194 ms                                                      | 174 ms: 1.12x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 858 us: 1.12x faster                                                        |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 189 ms: 1.08x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.40 us: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 36.9 ns: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.6 ms: 1.06x faster                                                       |
| sympy_expand             | 314 ms                                                      | 299 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.62 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                       |
| nbody                    | 71.3 ms                                                     | 69.1 ms: 1.03x faster                                                       |
| scimark_fft              | 187 ms                                                      | 183 ms: 1.02x faster                                                        |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                       |
| fannkuch                 | 256 ms                                                      | 262 ms: 1.02x slower                                                        |
| unpickle_list            | 2.71 us                                                     | 2.84 us: 1.04x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.9 us: 1.04x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.96 us: 1.08x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.2 us: 1.08x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.87 us: 1.15x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.79 ms: 1.22x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.5 ms: 1.24x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.04 ms: 1.45x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 90.8 ms: 1.46x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (3): meteor_contest, async_generators, logging_format
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.231x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown
# Results vs. 3.10.4

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-amd64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.230x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 217 ms: 2.43x faster                                                        |
| async_tree_none         | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 340 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.9 ms: 1.38x faster                                                       |
| nbody          | 71.3 ms                                                     | 68.9 ms: 1.03x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.6 ms: 1.21x faster                                                       |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.85 ms: 1.34x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 229 us: 1.18x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 40.1 ms: 1.11x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.47 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.2 ms: 1.01x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.79 us: 1.03x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| pickle               | 6.85 us                                                     | 7.76 us: 1.13x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 20.4 us: 1.19x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.50 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.95 ms: 1.30x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.6 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.19x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 217 ms: 2.43x faster                                                        |
| async_tree_none          | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 34.6 ms: 2.19x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 340 ms: 1.87x faster                                                        |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                        |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                       |
| go                       | 139 ms                                                      | 86.1 ms: 1.61x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 462 ms: 1.59x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 60.8 ns: 1.56x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.36 sec: 1.55x faster                                                      |
| richards_super           | 52.2 ms                                                     | 34.4 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.8 ms: 1.48x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.47x faster                                                       |
| raytrace                 | 273 ms                                                      | 192 ms: 1.43x faster                                                        |
| richards                 | 42.4 ms                                                     | 29.9 ms: 1.42x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.3 us: 1.42x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 862 us: 1.41x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.38x faster                                                       |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.38x faster                                                       |
| deepcopy                 | 255 us                                                      | 186 us: 1.37x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 63.2 ms: 1.36x faster                                                       |
| pyflate                  | 409 ms                                                      | 304 ms: 1.34x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.85 ms: 1.34x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.35 ms: 1.32x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 59.1 ms: 1.31x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.95 ms: 1.30x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.7 ms: 1.28x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.5 ms: 1.26x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| scimark_sor              | 106 ms                                                      | 84.5 ms: 1.26x faster                                                       |
| pycparser                | 930 ms                                                      | 741 ms: 1.25x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                       |
| thrift                   | 617 us                                                      | 507 us: 1.22x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                       |
| regex_compile            | 106 ms                                                      | 87.6 ms: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.0 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.2 ms: 1.20x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.6 ms: 1.20x faster                                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 229 us: 1.18x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 34.9 ms: 1.14x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 852 us: 1.12x faster                                                        |
| sympy_str                | 194 ms                                                      | 174 ms: 1.12x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.60 sec: 1.11x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 40.1 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 549 ms: 1.08x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.47 us: 1.07x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                        |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.07x faster                                                        |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.4 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.62 ms: 1.04x faster                                                       |
| nbody                    | 71.3 ms                                                     | 68.9 ms: 1.03x faster                                                       |
| scimark_fft              | 187 ms                                                      | 182 ms: 1.03x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.5 ms: 1.01x faster                                                       |
| async_generators         | 222 ms                                                      | 220 ms: 1.01x faster                                                        |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 56.2 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.89 us: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.79 us: 1.03x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.45 us: 1.04x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                                        |
| unpack_sequence          | 39.6 ns                                                     | 43.4 ns: 1.09x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.76 us: 1.13x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.4 us: 1.19x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.3 ms: 1.21x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.78 ms: 1.21x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.50 us: 1.27x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 86.2 ms: 1.39x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.02 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.230x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown
# Results vs. 3.10.4

- fork: python
- ref: e1baa778f602ede66831
- machine: windows-amd64
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.195x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 408 ms: 2.72x faster                                                        |
| async_tree_none         | 435 ms                                                      | 182 ms: 2.39x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 225 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 352 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.8 ms: 1.19x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 75.9 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.4 ms: 1.23x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| regex_dna      | 136 ms                                                      | 124 ms: 1.09x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 24.6 ms: 1.59x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.70 ms: 1.37x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.25x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 222 us: 1.21x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 86.7 ms: 1.12x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.1 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 57.0 ms: 1.03x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.77 ms: 1.33x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.7 ms: 1.19x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 408 ms: 2.72x faster                                                        |
| async_tree_none          | 435 ms                                                      | 182 ms: 2.39x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 225 ms: 2.34x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 352 ms: 1.81x faster                                                        |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                        |
| go                       | 139 ms                                                      | 88.2 ms: 1.58x faster                                                       |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.4 ns: 1.52x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.8 ms: 1.50x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.5 us: 1.40x faster                                                       |
| deepcopy                 | 255 us                                                      | 183 us: 1.40x faster                                                        |
| raytrace                 | 273 ms                                                      | 197 ms: 1.39x faster                                                        |
| richards                 | 42.4 ms                                                     | 30.7 ms: 1.38x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.70 ms: 1.37x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 63.2 ms: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 900 us: 1.35x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.77 ms: 1.33x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.8 ms: 1.31x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.30x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.44 ms: 1.29x faster                                                       |
| pyflate                  | 409 ms                                                      | 319 ms: 1.28x faster                                                        |
| pycparser                | 930 ms                                                      | 732 ms: 1.27x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.25x faster                                                        |
| regex_compile            | 106 ms                                                      | 86.4 ms: 1.23x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 222 us: 1.21x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 63.7 ms: 1.21x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.19x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                       |
| float                    | 61.7 ms                                                     | 51.8 ms: 1.19x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.2 ms: 1.19x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.7 ms: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.7 ms: 1.18x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                      |
| scimark_sor              | 106 ms                                                      | 91.3 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 825 us: 1.16x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.08 sec: 1.13x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 86.7 ms: 1.12x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.7 ms: 1.12x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.1 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| regex_dna                | 136 ms                                                      | 124 ms: 1.09x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 541 ms: 1.09x faster                                                        |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| json                     | 3.14 ms                                                     | 2.91 ms: 1.08x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 65.1 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.65 us: 1.02x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.70 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.25 us: 1.00x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.5 ms: 1.02x slower                                                       |
| scimark_fft              | 187 ms                                                      | 191 ms: 1.02x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 57.0 ms: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                                        |
| nbody                    | 71.3 ms                                                     | 75.9 ms: 1.07x slower                                                       |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| mypy2                    | 555 ms                                                      | 639 ms: 1.15x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.77 ms: 1.21x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.3 ms: 1.21x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.3 ms: 1.33x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.52x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 24.6 ms: 1.59x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.195x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown
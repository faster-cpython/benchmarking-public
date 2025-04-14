# Results vs. 3.10.4

- fork: python
- ref: 555dc50c811e3e9ebdc3
- machine: windows-amd64
- commit hash: 555dc50
- commit date: 2025-02-06
- overall geometric mean: 1.231x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 423 ms: 2.62x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 223 ms: 2.36x faster                                                        |
| async_tree_none         | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.8 ms: 1.35x faster                                                       |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.6 ms: 1.24x faster                                                       |
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.72 ms: 1.36x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 218 us: 1.24x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.5 ms: 1.12x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.5 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.74 ms: 1.34x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.19x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 423 ms: 2.62x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 223 ms: 2.36x faster                                                        |
| async_tree_none          | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.15 ms: 1.95x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 57.8 ns: 1.64x faster                                                       |
| go                       | 139 ms                                                      | 85.7 ms: 1.62x faster                                                       |
| generators               | 32.4 ms                                                     | 20.2 ms: 1.60x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.8 ms: 1.59x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.2 us: 1.50x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.49x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                       |
| richards                 | 42.4 ms                                                     | 28.7 ms: 1.48x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 852 us: 1.43x faster                                                        |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 60.8 ms: 1.41x faster                                                       |
| deepcopy                 | 255 us                                                      | 183 us: 1.40x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.40x faster                                                       |
| pyflate                  | 409 ms                                                      | 296 ms: 1.38x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.72 ms: 1.36x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.24 ms: 1.36x faster                                                       |
| float                    | 61.7 ms                                                     | 45.8 ms: 1.35x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.74 ms: 1.34x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.9 ms: 1.33x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.0 ms: 1.33x faster                                                       |
| pycparser                | 930 ms                                                      | 717 ms: 1.30x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.7 ms: 1.28x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                       |
| scimark_sor              | 106 ms                                                      | 85.4 ms: 1.24x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 60.9 ms: 1.24x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 218 us: 1.24x faster                                                        |
| coroutines               | 16.0 ms                                                     | 12.9 ms: 1.24x faster                                                       |
| regex_compile            | 106 ms                                                      | 85.6 ms: 1.24x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| thrift                   | 617 us                                                      | 510 us: 1.21x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.5 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.2 ms: 1.19x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.19x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.17x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 34.9 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 847 us: 1.13x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.13x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 39.5 ms: 1.12x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 527 ms: 1.12x faster                                                        |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 189 ms: 1.09x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 62.0 ms: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                                       |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.63 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                       |
| scimark_fft              | 187 ms                                                      | 185 ms: 1.02x faster                                                        |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.33 us: 1.02x slower                                                       |
| fannkuch                 | 256 ms                                                      | 262 ms: 1.02x slower                                                        |
| json                     | 3.14 ms                                                     | 3.21 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.5 us: 1.11x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.70 ms: 1.19x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.7 ms: 1.22x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.00 ms: 1.42x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.4 ms: 1.44x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (4): logging_format, meteor_contest, async_generators, nbody
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250206-3.14.0a4+-555dc50/bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.231x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown
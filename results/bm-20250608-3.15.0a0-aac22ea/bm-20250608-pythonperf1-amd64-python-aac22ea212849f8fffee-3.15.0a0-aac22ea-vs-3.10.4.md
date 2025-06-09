# Results vs. 3.10.4

- fork: python
- ref: aac22ea212849f8fffee
- machine: windows-amd64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.158x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 402 ms: 2.76x faster                                                       |
| async_tree_none         | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 212 ms: 2.49x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.40x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                      |
| nbody          | 71.3 ms                                                     | 64.8 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.5 ms: 1.32x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.33 ms: 1.45x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.0 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.17x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 402 ms: 2.76x faster                                                       |
| async_tree_none          | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 212 ms: 2.49x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                                      |
| mdp                      | 1.78 sec                                                    | 815 ms: 2.18x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                      |
| go                       | 139 ms                                                      | 77.0 ms: 1.80x faster                                                      |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                                      |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.57x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.0 ms: 1.54x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.53x faster                                                      |
| raytrace                 | 273 ms                                                      | 183 ms: 1.50x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                      |
| deepcopy                 | 255 us                                                      | 172 us: 1.49x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.6 ms: 1.47x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.33 ms: 1.45x faster                                                      |
| scimark_sor              | 106 ms                                                      | 74.5 ms: 1.42x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.04 ms: 1.42x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.4 ms: 1.42x faster                                                      |
| pyflate                  | 409 ms                                                      | 289 ms: 1.42x faster                                                       |
| float                    | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 57.5 ms: 1.34x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.3 ms: 1.32x faster                                                      |
| regex_compile            | 106 ms                                                      | 80.5 ms: 1.32x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| pycparser                | 930 ms                                                      | 720 ms: 1.29x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.1 ms: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                     |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| nbody                    | 71.3 ms                                                     | 64.8 ms: 1.10x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 541 ms: 1.09x faster                                                       |
| scimark_fft              | 187 ms                                                      | 173 ms: 1.09x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.4 ms: 1.08x faster                                                      |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.54 ms: 1.07x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.9 ms: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.02x faster                                                      |
| fannkuch                 | 256 ms                                                      | 253 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.81 us: 1.01x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.33 us: 1.02x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.0 ms: 1.03x slower                                                      |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.71 ms: 1.20x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 315 ns: 3.33x slower                                                       |
| coverage                 | 39.0 ms                                                     | 299 ms: 7.66x slower                                                       |
| thrift                   | 617 us                                                      | 93.6 ms: 151.63x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.158x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown
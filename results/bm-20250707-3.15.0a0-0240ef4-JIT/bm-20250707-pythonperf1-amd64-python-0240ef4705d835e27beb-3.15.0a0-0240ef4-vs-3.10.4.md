# Results vs. 3.10.4

- fork: python
- ref: 0240ef4705d835e27beb
- machine: windows-amd64
- commit hash: 0240ef4
- commit date: 2025-07-07
- overall geometric mean: 1.320x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_none         | 435 ms                                                      | 168 ms: 2.60x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 55.0 ms: 1.30x faster                                                      |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.3 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.70x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.13 sec: 1.47x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 202 us: 1.33x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.8 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.40 ms: 1.67x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.9 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_none          | 435 ms                                                      | 168 ms: 2.60x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.6 ms: 2.39x faster                                                      |
| mdp                      | 1.78 sec                                                    | 799 ms: 2.23x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                      |
| go                       | 139 ms                                                      | 76.2 ms: 1.82x faster                                                      |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| richards_super           | 52.2 ms                                                     | 29.9 ms: 1.74x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 54.4 ns: 1.74x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.70x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.40 ms: 1.67x faster                                                      |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                      |
| pyflate                  | 409 ms                                                      | 253 ms: 1.62x faster                                                       |
| richards                 | 42.4 ms                                                     | 26.3 ms: 1.61x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.9 us: 1.61x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.55x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                                      |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.13 sec: 1.47x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.9 ms: 1.44x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 60.1 ms: 1.43x faster                                                      |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.15 ms: 1.38x faster                                                      |
| scimark_sor              | 106 ms                                                      | 77.2 ms: 1.38x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.3 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.4 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 691 ms: 1.35x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 202 us: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 931 ms: 1.31x faster                                                       |
| nbody                    | 71.3 ms                                                     | 55.0 ms: 1.30x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 460 ms: 1.29x faster                                                       |
| thrift                   | 617 us                                                      | 484 us: 1.28x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                      |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.23x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.4 ms: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.27 ms: 1.20x faster                                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.9 ms: 1.18x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                     |
| fannkuch                 | 256 ms                                                      | 222 ms: 1.15x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 68.2 ms: 1.13x faster                                                      |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.3 ms: 1.12x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.8 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.4 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 294 ms: 1.07x faster                                                       |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.51 us: 1.04x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.02 us: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.34 ms: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 247 ms: 1.12x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.0 ms: 1.31x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.50x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                               |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250707-3.15.0a0-0240ef4-JIT/bm-20250707-pythonperf1-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.320x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown
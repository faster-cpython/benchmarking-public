# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 392 ms: 2.83x faster                                                       |
| async_tree_none         | 435 ms                                                      | 166 ms: 2.62x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 202 ms: 2.61x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 332 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.47x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| nbody          | 71.3 ms                                                     | 54.5 ms: 1.31x faster                                                      |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.75x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.10 sec: 1.52x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 203 us: 1.33x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 34.9 ms: 1.27x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.7 ms: 1.10x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.54 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 7.68 us: 1.12x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.6 us: 1.14x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.0 ms: 1.22x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.32 ms: 1.70x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.33x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 392 ms: 2.83x faster                                                       |
| async_tree_none          | 435 ms                                                      | 166 ms: 2.62x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 202 ms: 2.61x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.1 ms: 2.52x faster                                                      |
| mdp                      | 1.78 sec                                                    | 802 ms: 2.22x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 332 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                      |
| go                       | 139 ms                                                      | 75.7 ms: 1.83x faster                                                      |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.75x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.0 ns: 1.75x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.32 ms: 1.70x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.8 ms: 1.64x faster                                                      |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.63x faster                                                      |
| pyflate                  | 409 ms                                                      | 251 ms: 1.63x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.60x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.3 ms: 1.53x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.10 sec: 1.52x faster                                                     |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                       |
| richards                 | 42.4 ms                                                     | 28.1 ms: 1.51x faster                                                      |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.42 sec: 1.48x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 59.2 ms: 1.45x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 506 ms: 1.45x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.98 ms: 1.44x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.1 ms: 1.43x faster                                                      |
| float                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| scimark_sor              | 106 ms                                                      | 76.7 ms: 1.38x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.3 ms: 1.35x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 695 ms: 1.34x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 911 ms: 1.34x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 203 us: 1.33x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 450 ms: 1.31x faster                                                       |
| nbody                    | 71.3 ms                                                     | 54.5 ms: 1.31x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 34.9 ms: 1.27x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                                      |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                      |
| thrift                   | 617 us                                                      | 500 us: 1.23x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.6 ms: 1.22x faster                                                      |
| fannkuch                 | 256 ms                                                      | 211 ms: 1.21x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.28 ms: 1.19x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 33.3 ns: 1.19x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 64.9 ms: 1.19x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                     |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.3 ms: 1.12x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                      |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 862 us: 1.11x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.7 ms: 1.10x faster                                                      |
| sympy_expand             | 314 ms                                                      | 290 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 70.5 ms: 1.08x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.54 us: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.54 us: 1.03x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.03 us: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                      |
| json                     | 3.14 ms                                                     | 3.09 ms: 1.01x faster                                                      |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.24 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 243 ms: 1.09x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.68 us: 1.12x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.6 us: 1.14x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.0 ms: 1.22x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.10 ms: 1.49x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 94.3 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.29x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.321x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown
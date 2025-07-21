# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.142x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.87 sec: 1.50x slower                                                     |
| html5lib       | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 352 ms: 3.15x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.52x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.48x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.6 ms: 1.32x faster                                                      |
| pidigits       | 149 ms                                                      | 138 ms: 1.08x faster                                                       |
| nbody          | 71.3 ms                                                     | 81.0 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| regex_compile  | 106 ms                                                      | 94.6 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.68 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.69 ms: 1.37x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 156 us: 1.18x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 239 us: 1.13x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.1 ms: 1.10x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 45.2 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.8 us: 1.12x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.09 us: 1.12x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 63.0 ms: 1.13x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.12 us: 1.15x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.5 us: 1.16x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.2 us: 1.18x slower                                                      |
| pickle               | 6.85 us                                                     | 8.18 us: 1.19x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.66 sec: 1.59x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 20.3 ms: 1.03x slower                                                      |
| genshi_xml      | 41.0 ms                                                     | 42.7 ms: 1.04x slower                                                      |
| mako            | 9.03 ms                                                     | 9.63 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 352 ms: 3.15x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 130 us: 2.58x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.52x faster                                                       |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.5 ms: 2.48x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.44 ms: 1.72x faster                                                      |
| pylint                   | 350 ms                                                      | 207 ms: 1.69x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 461 ms: 1.59x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.15 sec: 1.55x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 61.8 ns: 1.53x faster                                                      |
| go                       | 139 ms                                                      | 94.5 ms: 1.47x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.33 us: 1.43x faster                                                      |
| generators               | 32.4 ms                                                     | 22.6 ms: 1.43x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.38x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.69 ms: 1.37x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.4 us: 1.34x faster                                                      |
| richards_super           | 52.2 ms                                                     | 39.1 ms: 1.33x faster                                                      |
| chaos                    | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                      |
| float                    | 61.7 ms                                                     | 46.6 ms: 1.32x faster                                                      |
| raytrace                 | 273 ms                                                      | 209 ms: 1.31x faster                                                       |
| pyflate                  | 409 ms                                                      | 315 ms: 1.30x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 66.2 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 731 ms: 1.27x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.6 ms: 1.26x faster                                                      |
| deepcopy                 | 255 us                                                      | 203 us: 1.26x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.61 ms: 1.25x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.15 ms: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.6 ms: 1.21x faster                                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| scimark_sor              | 106 ms                                                      | 90.0 ms: 1.18x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 156 us: 1.18x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.8 ms: 1.13x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 239 us: 1.13x faster                                                       |
| regex_compile            | 106 ms                                                      | 94.6 ms: 1.12x faster                                                      |
| sympy_sum                | 107 ms                                                      | 97.1 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.1 ms: 1.10x faster                                                      |
| thrift                   | 617 us                                                      | 566 us: 1.09x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 57.4 ms: 1.09x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| pidigits                 | 149 ms                                                      | 138 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 231 ms: 1.06x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 73.6 ms: 1.05x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 571 ms: 1.04x faster                                                       |
| sympy_str                | 194 ms                                                      | 188 ms: 1.04x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.13 us: 1.03x faster                                                      |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.68 ms: 1.01x slower                                                      |
| xml_etree_process        | 44.5 ms                                                     | 45.2 ms: 1.02x slower                                                      |
| sympy_expand             | 314 ms                                                      | 320 ms: 1.02x slower                                                       |
| genshi_text              | 19.8 ms                                                     | 20.3 ms: 1.03x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 42.7 ms: 1.04x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 41.6 ns: 1.05x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.63 ms: 1.07x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.33 us: 1.08x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.80 us: 1.09x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 73.1 ms: 1.10x slower                                                      |
| json_loads               | 14.0 us                                                     | 15.8 us: 1.12x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.09 us: 1.12x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 63.0 ms: 1.13x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.09 ms: 1.14x slower                                                      |
| nbody                    | 71.3 ms                                                     | 81.0 ms: 1.14x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.11 ms: 1.14x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.12 us: 1.15x slower                                                      |
| scimark_fft              | 187 ms                                                      | 216 ms: 1.16x slower                                                       |
| unpickle                 | 9.09 us                                                     | 10.5 us: 1.16x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 88.2 ms: 1.16x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.2 us: 1.18x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.18 us: 1.19x slower                                                      |
| fannkuch                 | 256 ms                                                      | 307 ms: 1.20x slower                                                       |
| async_generators         | 222 ms                                                      | 275 ms: 1.24x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 79.1 ms: 1.28x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.04 ms: 1.29x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.39 ms: 1.37x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.72 sec: 1.41x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.87 sec: 1.50x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.66 sec: 1.59x slower                                                     |
| coverage                 | 39.0 ms                                                     | 68.3 ms: 1.75x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.142x faster

# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
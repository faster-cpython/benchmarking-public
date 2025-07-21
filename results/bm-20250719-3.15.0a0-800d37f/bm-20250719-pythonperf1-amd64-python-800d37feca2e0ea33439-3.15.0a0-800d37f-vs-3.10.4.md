# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.289x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 392 ms: 2.83x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 202 ms: 2.61x faster                                                       |
| async_tree_none         | 435 ms                                                      | 168 ms: 2.59x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.47x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.7 ms: 1.45x faster                                                      |
| nbody          | 71.3 ms                                                     | 65.5 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.17 ms: 1.48x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.39x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.4 ms: 1.10x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.65 us: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 54.9 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.95 us: 1.09x slower                                                      |
| pickle               | 6.85 us                                                     | 7.85 us: 1.15x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.1 us: 1.17x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.42 us: 1.24x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.44 ms: 1.40x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                      |
| django_template | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.31x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 392 ms: 2.83x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 202 ms: 2.61x faster                                                       |
| async_tree_none          | 435 ms                                                      | 168 ms: 2.59x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.4 ms: 2.49x faster                                                      |
| mdp                      | 1.78 sec                                                    | 804 ms: 2.22x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.17 ms: 1.93x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 400 ms: 1.83x faster                                                       |
| go                       | 139 ms                                                      | 77.0 ms: 1.81x faster                                                      |
| pylint                   | 350 ms                                                      | 195 ms: 1.79x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.1 ns: 1.72x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.0 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.27 sec: 1.66x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 17.5 us: 1.64x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| deepcopy                 | 255 us                                                      | 167 us: 1.53x faster                                                       |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.9 ms: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.17 ms: 1.48x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.3 ms: 1.47x faster                                                      |
| float                    | 61.7 ms                                                     | 42.7 ms: 1.45x faster                                                      |
| pyflate                  | 409 ms                                                      | 285 ms: 1.43x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.03 ms: 1.42x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.44 ms: 1.40x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.1 ms: 1.40x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.39x faster                                                       |
| scimark_sor              | 106 ms                                                      | 77.0 ms: 1.38x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 699 ms: 1.33x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 48.7 ms: 1.29x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                      |
| thrift                   | 617 us                                                      | 496 us: 1.24x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.6 ms: 1.22x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.22x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 490 ms: 1.21x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 65.6 ms: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                                      |
| sympy_str                | 194 ms                                                      | 168 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 843 us: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                      |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| sympy_expand             | 314 ms                                                      | 284 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.48 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.4 ms: 1.10x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 36.3 ns: 1.09x faster                                                      |
| nbody                    | 71.3 ms                                                     | 65.5 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.5 ms: 1.08x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.9 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.65 us: 1.05x faster                                                      |
| json                     | 3.14 ms                                                     | 2.99 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.46 us: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.04 us: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 54.9 ms: 1.01x faster                                                      |
| scimark_fft              | 187 ms                                                      | 189 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                                       |
| fannkuch                 | 256 ms                                                      | 270 ms: 1.06x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.95 us: 1.09x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.47 ms: 1.14x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.85 us: 1.15x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.1 us: 1.17x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.42 us: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.6 ms: 1.27x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 94.5 ms: 1.52x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.16 ms: 1.53x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.289x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown
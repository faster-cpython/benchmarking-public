# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.183x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.1 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 210 ms: 2.07x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 258 ms: 2.04x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 579 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 82.8 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.9 ms: 1.17x faster                                                      |
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 15.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.25 ms: 1.47x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.28x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.5 ms: 1.10x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 95.0 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.1 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.90 ms: 1.31x faster                                                      |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.1 ms: 1.14x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.04x faster                                                       |
| async_tree_none          | 435 ms                                                      | 210 ms: 2.07x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 258 ms: 2.04x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 579 ms: 1.91x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| go                       | 139 ms                                                      | 85.1 ms: 1.63x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| pylint                   | 350 ms                                                      | 224 ms: 1.56x faster                                                       |
| generators               | 32.4 ms                                                     | 21.1 ms: 1.54x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 63.7 ns: 1.49x faster                                                      |
| raytrace                 | 273 ms                                                      | 185 ms: 1.48x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.25 ms: 1.47x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.0 ms: 1.45x faster                                                      |
| chaos                    | 61.7 ms                                                     | 42.8 ms: 1.44x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.0 us: 1.44x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 61.2 ms: 1.40x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 529 ms: 1.38x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.38x faster                                                      |
| deepcopy                 | 255 us                                                      | 186 us: 1.38x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 886 us: 1.37x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                      |
| richards                 | 42.4 ms                                                     | 31.8 ms: 1.34x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.37 ms: 1.31x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.90 ms: 1.31x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 48.5 ms: 1.29x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                      |
| pyflate                  | 409 ms                                                      | 321 ms: 1.27x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.66 sec: 1.27x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                       |
| thrift                   | 617 us                                                      | 514 us: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.6 ms: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.5 ms: 1.19x faster                                                      |
| scimark_sor              | 106 ms                                                      | 89.4 ms: 1.19x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.18x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 66.0 ms: 1.17x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.0 ms: 1.17x faster                                                      |
| regex_compile            | 106 ms                                                      | 90.9 ms: 1.17x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.1 ms: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 828 us: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 36.1 ms: 1.14x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                      |
| pycparser                | 930 ms                                                      | 833 ms: 1.12x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.9 ms: 1.11x faster                                                      |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                       |
| float                    | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 40.5 ms: 1.10x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.08x faster                                                     |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 551 ms: 1.08x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 63.8 ms: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 303 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.63 ms: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| json                     | 3.14 ms                                                     | 3.07 ms: 1.02x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 95.0 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.7 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.1 ms: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.91 us: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.5 ms: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.45 us: 1.04x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.2 ms: 1.05x slower                                                      |
| scimark_fft              | 187 ms                                                      | 197 ms: 1.05x slower                                                       |
| python_startup           | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| fannkuch                 | 256 ms                                                      | 288 ms: 1.13x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 70.6 ms: 1.14x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 917 us: 1.15x slower                                                       |
| nbody                    | 71.3 ms                                                     | 82.8 ms: 1.16x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.7 ms: 1.25x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.30 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                               |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.183x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown
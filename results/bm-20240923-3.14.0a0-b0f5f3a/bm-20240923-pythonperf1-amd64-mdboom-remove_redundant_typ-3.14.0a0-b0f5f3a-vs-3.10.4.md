# Results vs. 3.10.4

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-amd64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                      |
| tornado_http   | 108 ms                                                      | 84.2 ms: 1.29x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 209 ms: 2.09x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 265 ms: 1.99x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 570 ms: 1.95x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.8 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 81.8 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| regex_compile  | 106 ms                                                      | 91.4 ms: 1.16x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.26x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.34 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.3 ms: 1.03x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.31 us: 1.07x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.07 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                      |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.5 ms: 1.09x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                                       |
| async_tree_none          | 435 ms                                                      | 209 ms: 2.09x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 265 ms: 1.99x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 570 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.84x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| go                       | 139 ms                                                      | 86.6 ms: 1.60x faster                                                      |
| pylint                   | 350 ms                                                      | 224 ms: 1.56x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 474 ms: 1.54x faster                                                       |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 63.0 ns: 1.50x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| richards_super           | 52.2 ms                                                     | 35.6 ms: 1.47x faster                                                      |
| chaos                    | 61.7 ms                                                     | 42.6 ms: 1.45x faster                                                      |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 61.3 ms: 1.40x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.38x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.37x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 895 us: 1.36x faster                                                       |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.0 ms: 1.32x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.62 sec: 1.31x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.42 ms: 1.30x faster                                                      |
| tornado_http             | 108 ms                                                      | 84.2 ms: 1.29x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                      |
| pyflate                  | 409 ms                                                      | 322 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 734 ms: 1.27x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.26x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.25x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.9 ms: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 807 us: 1.19x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.0 ms: 1.17x faster                                                      |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.64 us: 1.17x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.16x faster                                                      |
| regex_compile            | 106 ms                                                      | 91.4 ms: 1.16x faster                                                      |
| scimark_sor              | 106 ms                                                      | 92.2 ms: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.96 us: 1.13x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 69.0 ms: 1.12x faster                                                      |
| float                    | 61.7 ms                                                     | 55.8 ms: 1.11x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.10x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 37.5 ms: 1.09x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 543 ms: 1.09x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.60 ms: 1.05x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.05x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 63.8 ms: 1.04x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.91 us: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.8 ms: 1.03x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.34 us: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.3 ms: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.46 us: 1.04x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.31 us: 1.07x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 66.3 ms: 1.07x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| scimark_fft              | 187 ms                                                      | 203 ms: 1.08x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.09x slower                                                      |
| async_generators         | 222 ms                                                      | 241 ms: 1.09x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 883 us: 1.10x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.07 us: 1.11x slower                                                      |
| fannkuch                 | 256 ms                                                      | 293 ms: 1.14x slower                                                       |
| nbody                    | 71.3 ms                                                     | 81.8 ms: 1.15x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 46.4 ns: 1.17x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.3 ms: 1.19x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.05 ms: 1.28x slower                                                      |
| json                     | 3.14 ms                                                     | 4.39 ms: 1.40x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, pathlib
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown
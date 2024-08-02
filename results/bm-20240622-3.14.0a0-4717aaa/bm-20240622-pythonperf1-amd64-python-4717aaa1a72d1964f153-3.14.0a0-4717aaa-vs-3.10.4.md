# Results vs. 3.10.4

- fork: python
- ref: 4717aaa1a72d1964f153
- machine: windows-amd64
- commit hash: 4717aaa
- commit date: 2024-06-22
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 211 ms: 1.17x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 35.0 ms: 1.46x faster                                                      |
| tornado_http   | 108 ms                                                      | 79.7 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.29x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 503 ms: 2.21x faster                                                       |
| async_tree_none         | 435 ms                                                      | 199 ms: 2.19x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 243 ms: 2.17x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 380 ms: 1.68x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.05x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 49.1 ms: 1.26x faster                                                      |
| nbody          | 71.3 ms                                                     | 65.8 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.2 ms: 1.37x faster                                                      |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.82 ms: 1.57x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 181 us: 1.49x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.47x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.9 ms: 1.21x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.59 us: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.0 ms: 1.05x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.02x faster                                                      |
| pickle               | 6.85 us                                                     | 7.10 us: 1.04x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.84 us: 1.05x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.2 us: 1.06x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.92 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 16.8 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.60 ms: 1.37x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                      |
| django_template | 28.9 ms                                                     | 22.1 ms: 1.31x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 31.8 ms: 1.29x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.28x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 503 ms: 2.21x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.90 ms: 2.20x faster                                                      |
| async_tree_none          | 435 ms                                                      | 199 ms: 2.19x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 243 ms: 2.17x faster                                                       |
| richards_super           | 52.2 ms                                                     | 29.4 ms: 1.78x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 53.6 ns: 1.76x faster                                                      |
| pylint                   | 350 ms                                                      | 204 ms: 1.72x faster                                                       |
| raytrace                 | 273 ms                                                      | 159 ms: 1.71x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 17.1 us: 1.69x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 380 ms: 1.68x faster                                                       |
| go                       | 139 ms                                                      | 83.6 ms: 1.66x faster                                                      |
| richards                 | 42.4 ms                                                     | 25.9 ms: 1.64x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.62x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.2 ms: 1.62x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 53.4 ms: 1.61x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 771 us: 1.58x faster                                                       |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.58x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.82 ms: 1.57x faster                                                      |
| deepcopy                 | 255 us                                                      | 164 us: 1.56x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.70 ms: 1.55x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 473 ms: 1.55x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 966 us: 1.53x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 181 us: 1.49x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.47x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 35.0 ms: 1.46x faster                                                      |
| pyflate                  | 409 ms                                                      | 281 ms: 1.46x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.42x faster                                                      |
| scimark_sor              | 106 ms                                                      | 75.4 ms: 1.41x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 45.1 ms: 1.39x faster                                                      |
| regex_compile            | 106 ms                                                      | 77.2 ms: 1.37x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.60 ms: 1.37x faster                                                      |
| tornado_http             | 108 ms                                                      | 79.7 ms: 1.36x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.57 sec: 1.34x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.68 us: 1.31x faster                                                      |
| django_template          | 28.9 ms                                                     | 22.1 ms: 1.31x faster                                                      |
| pycparser                | 930 ms                                                      | 719 ms: 1.29x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 742 us: 1.29x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 31.8 ms: 1.29x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.38 sec: 1.29x faster                                                     |
| sympy_sum                | 107 ms                                                      | 84.3 ms: 1.27x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 61.2 ms: 1.26x faster                                                      |
| float                    | 61.7 ms                                                     | 49.1 ms: 1.26x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.9 ms: 1.24x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 986 ms: 1.24x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 481 ms: 1.23x faster                                                       |
| thrift                   | 617 us                                                      | 504 us: 1.23x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 36.9 ms: 1.21x faster                                                      |
| sympy_str                | 194 ms                                                      | 162 ms: 1.20x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 33.1 ms: 1.20x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 55.8 ms: 1.19x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 176 ms: 1.17x faster                                                       |
| 2to3                     | 246 ms                                                      | 211 ms: 1.17x faster                                                       |
| sympy_expand             | 314 ms                                                      | 275 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| json                     | 3.14 ms                                                     | 2.88 ms: 1.09x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.22 us: 1.09x faster                                                      |
| nbody                    | 71.3 ms                                                     | 65.8 ms: 1.08x faster                                                      |
| scimark_fft              | 187 ms                                                      | 173 ms: 1.08x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.78 us: 1.08x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.6 ms: 1.07x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.59 us: 1.06x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.59 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.0 ms: 1.05x faster                                                      |
| fannkuch                 | 256 ms                                                      | 245 ms: 1.04x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.02x faster                                                      |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.10 us: 1.04x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.84 us: 1.05x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 65.3 ms: 1.05x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.2 us: 1.06x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.92 us: 1.06x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.8 ms: 1.08x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 914 us: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.8 ms: 1.20x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.93 ms: 1.25x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                               |

Benchmark hidden because not significant (3): pathlib, pidigits, python_startup
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown
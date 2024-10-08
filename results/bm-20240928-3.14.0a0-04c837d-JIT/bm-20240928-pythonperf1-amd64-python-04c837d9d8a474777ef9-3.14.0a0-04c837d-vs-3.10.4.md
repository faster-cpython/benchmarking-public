# Results vs. 3.10.4

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 248 ms: 1.01x slower                                                       |
| html5lib       | 51.0 ms                                                     | 42.1 ms: 1.21x faster                                                      |
| tornado_http   | 108 ms                                                      | 98.4 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 206 ms: 2.11x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 580 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 47.9 ms: 1.49x faster                                                      |
| float          | 61.7 ms                                                     | 45.2 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| regex_compile  | 106 ms                                                      | 94.1 ms: 1.13x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.72 ms: 1.60x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 201 us: 1.34x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 144 us: 1.27x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.0 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 94.6 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.79 us: 1.03x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 17.7 us: 1.03x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.77 us: 1.07x slower                                                      |
| pickle               | 6.85 us                                                     | 7.39 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                      |
| django_template | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 46.4 ms: 1.13x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.01x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.86 ms: 2.25x faster                                                      |
| async_tree_none          | 435 ms                                                      | 206 ms: 2.11x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.0 us: 1.92x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 580 ms: 1.91x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 44.0 ms: 1.76x faster                                                      |
| scimark_sor              | 106 ms                                                      | 61.9 ms: 1.71x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.1 ns: 1.66x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 38.7 ms: 1.62x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.72 ms: 1.60x faster                                                      |
| pyflate                  | 409 ms                                                      | 261 ms: 1.57x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 55.3 ms: 1.55x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.3 ms: 1.53x faster                                                      |
| nbody                    | 71.3 ms                                                     | 47.9 ms: 1.49x faster                                                      |
| go                       | 139 ms                                                      | 94.1 ms: 1.48x faster                                                      |
| generators               | 32.4 ms                                                     | 22.3 ms: 1.45x faster                                                      |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                       |
| float                    | 61.7 ms                                                     | 45.2 ms: 1.37x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 895 us: 1.36x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 545 ms: 1.34x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 201 us: 1.34x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.4 ms: 1.32x faster                                                      |
| raytrace                 | 273 ms                                                      | 210 ms: 1.30x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                     |
| pycparser                | 930 ms                                                      | 716 ms: 1.30x faster                                                       |
| pylint                   | 350 ms                                                      | 272 ms: 1.29x faster                                                       |
| scimark_fft              | 187 ms                                                      | 146 ms: 1.28x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 144 us: 1.27x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.15 ms: 1.27x faster                                                      |
| richards_super           | 52.2 ms                                                     | 41.7 ms: 1.25x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.18 ms: 1.25x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.71 sec: 1.23x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 42.1 ms: 1.21x faster                                                      |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.18x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.04 sec: 1.17x faster                                                     |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 826 us: 1.16x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 514 ms: 1.15x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.15x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 5.03 ms: 1.14x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.57 sec: 1.14x faster                                                     |
| regex_compile            | 106 ms                                                      | 94.1 ms: 1.13x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.0 ms: 1.11x faster                                                      |
| tornado_http             | 108 ms                                                      | 98.4 ms: 1.10x faster                                                      |
| richards                 | 42.4 ms                                                     | 38.7 ms: 1.10x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.5 ms: 1.08x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                      |
| fannkuch                 | 256 ms                                                      | 239 ms: 1.07x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| sympy_sum                | 107 ms                                                      | 102 ms: 1.04x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.48 us: 1.04x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.6 ms: 1.02x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.08 us: 1.02x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 205 ms: 1.00x faster                                                       |
| 2to3                     | 246 ms                                                      | 248 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.79 us: 1.03x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.7 us: 1.03x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.9 ms: 1.06x slower                                                      |
| sympy_expand             | 314 ms                                                      | 334 ms: 1.06x slower                                                       |
| python_startup           | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.77 us: 1.07x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.39 us: 1.08x slower                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 43.0 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.08x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.36 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 885 us: 1.11x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.4 ms: 1.13x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 72.9 ms: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.8 ms: 1.20x slower                                                      |
| async_generators         | 222 ms                                                      | 267 ms: 1.20x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 56.8 ns: 1.43x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (6): genshi_text, pidigits, sympy_integrate, docutils, meteor_contest, sympy_str
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown
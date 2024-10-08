# Results vs. 3.10.4

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-amd64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                      |
| tornado_http   | 108 ms                                                      | 83.3 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 207 ms: 2.11x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 564 ms: 1.96x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 388 ms: 1.64x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.93x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.4 ms: 1.13x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 79.8 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| regex_compile  | 106 ms                                                      | 89.6 ms: 1.18x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.18 ms: 1.48x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 145 us: 1.27x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.4 ms: 1.10x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.56 sec: 1.07x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.6 ms: 1.03x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.43 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.28 us: 1.06x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.94 us: 1.07x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.7 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.3 ms: 1.04x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.83 ms: 1.32x faster                                                      |
| django_template | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.9 ms: 1.14x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                       |
| async_tree_none          | 435 ms                                                      | 207 ms: 2.11x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 564 ms: 1.96x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 388 ms: 1.64x faster                                                       |
| go                       | 139 ms                                                      | 84.6 ms: 1.64x faster                                                      |
| pylint                   | 350 ms                                                      | 222 ms: 1.58x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 464 ms: 1.58x faster                                                       |
| generators               | 32.4 ms                                                     | 20.9 ms: 1.55x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 61.9 ns: 1.53x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.18 ms: 1.48x faster                                                      |
| raytrace                 | 273 ms                                                      | 187 ms: 1.46x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.3 ms: 1.46x faster                                                      |
| richards_super           | 52.2 ms                                                     | 35.8 ms: 1.46x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.44x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.0 us: 1.44x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.49 sec: 1.41x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 61.8 ms: 1.39x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 875 us: 1.39x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.35x faster                                                      |
| richards                 | 42.4 ms                                                     | 31.7 ms: 1.34x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.30 ms: 1.34x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.83 ms: 1.32x faster                                                      |
| tornado_http             | 108 ms                                                      | 83.3 ms: 1.30x faster                                                      |
| pyflate                  | 409 ms                                                      | 315 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 145 us: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 744 ms: 1.25x faster                                                       |
| thrift                   | 617 us                                                      | 507 us: 1.22x faster                                                       |
| scimark_sor              | 106 ms                                                      | 87.5 ms: 1.21x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.9 ms: 1.20x faster                                                      |
| sympy_sum                | 107 ms                                                      | 89.2 ms: 1.20x faster                                                      |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 64.7 ms: 1.19x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                                     |
| regex_compile            | 106 ms                                                      | 89.6 ms: 1.18x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 810 us: 1.18x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.5 ms: 1.18x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.18x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.9 ms: 1.14x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                      |
| float                    | 61.7 ms                                                     | 54.4 ms: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                     |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.0 ms: 1.11x faster                                                      |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.4 ms: 1.10x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 541 ms: 1.09x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.07x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.56 sec: 1.07x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.9 ms: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.6 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.64 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 73.9 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.66 us: 1.01x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.25 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.6 ms: 1.02x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.3 ms: 1.04x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.43 us: 1.04x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 41.3 ns: 1.04x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 65.8 ms: 1.06x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.28 us: 1.06x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.94 us: 1.07x slower                                                      |
| async_generators         | 222 ms                                                      | 238 ms: 1.07x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.52 ms: 1.08x slower                                                      |
| scimark_fft              | 187 ms                                                      | 204 ms: 1.09x slower                                                       |
| fannkuch                 | 256 ms                                                      | 280 ms: 1.09x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 887 us: 1.11x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                                      |
| nbody                    | 71.3 ms                                                     | 79.8 ms: 1.12x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.7 us: 1.15x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.1 ms: 1.23x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.06 ms: 1.29x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (2): json, xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown
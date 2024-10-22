# Results vs. 3.10.4

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.02x faster
- HPT reliability: 60.89%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 283 ms: 1.15x slower                                                       |
| docutils       | 1.92 sec                                                    | 2.18 sec: 1.14x slower                                                     |
| html5lib       | 51.0 ms                                                     | 47.9 ms: 1.07x faster                                                      |
| tornado_http   | 108 ms                                                      | 106 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 237 ms: 1.83x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 297 ms: 1.77x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 647 ms: 1.71x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 454 ms: 1.40x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.67x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.4 ms: 1.41x faster                                                      |
| float          | 61.7 ms                                                     | 55.8 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_compile  | 106 ms                                                      | 111 ms: 1.05x slower                                                       |
| regex_v8       | 15.4 ms                                                     | 16.9 ms: 1.10x slower                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.85 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.32 ms: 1.25x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.53 sec: 1.09x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 256 us: 1.05x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 47.1 ms: 1.06x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.92 us: 1.07x slower                                                      |
| unpickle_pure_python | 183 us                                                      | 204 us: 1.11x slower                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 109 ms: 1.12x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 75.4 ms: 1.16x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 64.6 ms: 1.16x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.3 us: 1.18x slower                                                      |
| pickle               | 6.85 us                                                     | 8.42 us: 1.23x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.41 us: 1.24x slower                                                      |
| unpickle             | 9.09 us                                                     | 11.9 us: 1.30x slower                                                      |
| json_loads           | 14.0 us                                                     | 20.7 us: 1.48x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.9 ms: 1.16x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.05 ms: 1.49x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 21.9 ms: 1.11x slower                                                      |
| django_template | 28.9 ms                                                     | 32.6 ms: 1.13x slower                                                      |
| genshi_xml      | 41.0 ms                                                     | 51.2 ms: 1.25x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 131 us: 2.56x faster                                                       |
| async_tree_none          | 435 ms                                                      | 237 ms: 1.83x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.30 ms: 1.82x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 297 ms: 1.77x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 647 ms: 1.71x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.6 us: 1.55x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.05 ms: 1.49x faster                                                      |
| nbody                    | 71.3 ms                                                     | 50.4 ms: 1.41x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 454 ms: 1.40x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.54 sec: 1.37x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 45.8 ms: 1.36x faster                                                      |
| pyflate                  | 409 ms                                                      | 301 ms: 1.36x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 59.8 ms: 1.29x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 569 ms: 1.29x faster                                                       |
| scimark_sor              | 106 ms                                                      | 83.8 ms: 1.27x faster                                                      |
| chaos                    | 61.7 ms                                                     | 48.9 ms: 1.26x faster                                                      |
| comprehensions           | 16.5 us                                                     | 13.2 us: 1.25x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 7.32 ms: 1.25x faster                                                      |
| generators               | 32.4 ms                                                     | 26.2 ms: 1.24x faster                                                      |
| go                       | 139 ms                                                      | 116 ms: 1.20x faster                                                       |
| deepcopy                 | 255 us                                                      | 214 us: 1.19x faster                                                       |
| richards_super           | 52.2 ms                                                     | 44.2 ms: 1.18x faster                                                      |
| pylint                   | 350 ms                                                      | 299 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 1.06 ms: 1.14x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.1 ms: 1.12x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 85.0 ns: 1.11x faster                                                      |
| pycparser                | 930 ms                                                      | 837 ms: 1.11x faster                                                       |
| float                    | 61.7 ms                                                     | 55.8 ms: 1.11x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.53 sec: 1.09x faster                                                     |
| raytrace                 | 273 ms                                                      | 253 ms: 1.08x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.37 ms: 1.08x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.78 us: 1.07x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 47.9 ms: 1.07x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.68 sec: 1.06x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 256 us: 1.05x faster                                                       |
| scimark_fft              | 187 ms                                                      | 180 ms: 1.04x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 49.2 ms: 1.03x faster                                                      |
| tornado_http             | 108 ms                                                      | 106 ms: 1.02x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 84.0 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.24 sec: 1.02x slower                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 2.25 us: 1.02x slower                                                      |
| pprint_safe_repr         | 592 ms                                                      | 612 ms: 1.03x slower                                                       |
| hexiom                   | 5.74 ms                                                     | 5.95 ms: 1.04x slower                                                      |
| regex_compile            | 106 ms                                                      | 111 ms: 1.05x slower                                                       |
| thrift                   | 617 us                                                      | 653 us: 1.06x slower                                                       |
| xml_etree_process        | 44.5 ms                                                     | 47.1 ms: 1.06x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.92 us: 1.07x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 82.0 ms: 1.08x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 83.1 ms: 1.09x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 16.9 ms: 1.10x slower                                                      |
| sympy_sum                | 107 ms                                                      | 118 ms: 1.10x slower                                                       |
| fannkuch                 | 256 ms                                                      | 282 ms: 1.10x slower                                                       |
| genshi_text              | 19.8 ms                                                     | 21.9 ms: 1.11x slower                                                      |
| unpickle_pure_python     | 183 us                                                      | 204 us: 1.11x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.85 ms: 1.12x slower                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 109 ms: 1.12x slower                                                       |
| django_template          | 28.9 ms                                                     | 32.6 ms: 1.13x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 75.6 ms: 1.13x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.18 sec: 1.14x slower                                                     |
| sympy_integrate          | 15.3 ms                                                     | 17.5 ms: 1.14x slower                                                      |
| 2to3                     | 246 ms                                                      | 283 ms: 1.15x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.81 us: 1.15x slower                                                      |
| python_startup           | 20.6 ms                                                     | 23.9 ms: 1.16x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 75.4 ms: 1.16x slower                                                      |
| sqlglot_normalize        | 205 ms                                                      | 239 ms: 1.16x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 64.6 ms: 1.16x slower                                                      |
| sympy_str                | 194 ms                                                      | 227 ms: 1.17x slower                                                       |
| json                     | 3.14 ms                                                     | 3.68 ms: 1.17x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.3 us: 1.18x slower                                                      |
| logging_simple           | 6.22 us                                                     | 7.36 us: 1.18x slower                                                      |
| coroutines               | 16.0 ms                                                     | 19.6 ms: 1.22x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.42 us: 1.23x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.41 us: 1.24x slower                                                      |
| sympy_expand             | 314 ms                                                      | 390 ms: 1.24x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 51.2 ms: 1.25x slower                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 50.0 ms: 1.25x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.01 ms: 1.27x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| unpickle                 | 9.09 us                                                     | 11.9 us: 1.30x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.19 ms: 1.32x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 82.8 ms: 1.33x slower                                                      |
| json_loads               | 14.0 us                                                     | 20.7 us: 1.48x slower                                                      |
| async_generators         | 222 ms                                                      | 336 ms: 1.51x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 61.0 ns: 1.54x slower                                                      |
| coverage                 | 39.0 ms                                                     | 60.8 ms: 1.56x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.24 ms: 1.59x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (2): bench_thread_pool, richards
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 60.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
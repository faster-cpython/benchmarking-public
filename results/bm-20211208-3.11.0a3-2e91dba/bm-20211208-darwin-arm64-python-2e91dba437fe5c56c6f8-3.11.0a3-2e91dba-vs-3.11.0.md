
# Results vs. 3.11.0

- fork: python
- ref: 2e91dba437fe5c56c6f8
- machine: darwin-arm64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.05x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| chameleon      | 4.57 ms                                                | 5.14 ms: 1.12x slower                                                 |
| docutils       | 1.47 sec                                               | 1.56 sec: 1.06x slower                                                |
| html5lib       | 34.7 ms                                                | 36.9 ms: 1.06x slower                                                 |
| tornado_http   | 72.4 ms                                                | 79.7 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 65.2 ms: 1.00x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| float          | 53.0 ms                                                | 56.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.50 ms: 1.05x faster                                                 |
| regex_compile  | 76.7 ms                                                | 78.4 ms: 1.02x slower                                                 |
| regex_dna      | 152 ms                                                 | 163 ms: 1.07x slower                                                  |
| regex_v8       | 16.2 ms                                                | 18.0 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 96.5 ms: 1.10x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.50 us: 1.05x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 67.2 ms: 1.03x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| xml_etree_generate   | 48.8 ms                                                | 49.9 ms: 1.02x slower                                                 |
| json_dumps           | 7.72 ms                                                | 7.91 ms: 1.02x slower                                                 |
| pickle               | 7.17 us                                                | 7.42 us: 1.04x slower                                                 |
| json_loads           | 16.1 us                                                | 16.8 us: 1.04x slower                                                 |
| unpickle             | 9.70 us                                                | 10.1 us: 1.04x slower                                                 |
| xml_etree_process    | 35.2 ms                                                | 37.5 ms: 1.06x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 177 us: 1.11x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 224 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 6.93 ms: 1.34x faster                                                 |
| python_startup         | 11.5 ms                                                | 12.7 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.53 ms: 1.00x slower                                                 |
| genshi_text     | 15.3 ms                                                | 16.1 ms: 1.06x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 32.4 ms: 1.09x slower                                                 |
| django_template | 21.0 ms                                                | 23.1 ms: 1.10x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site  | 9.31 ms                                                | 6.93 ms: 1.34x faster                                                 |
| pathlib                 | 27.8 ms                                                | 21.1 ms: 1.32x faster                                                 |
| coverage                | 58.6 ms                                                | 45.2 ms: 1.30x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 96.5 ms: 1.10x faster                                                 |
| generators              | 28.8 ms                                                | 27.3 ms: 1.06x faster                                                 |
| unpickle_list           | 2.63 us                                                | 2.50 us: 1.05x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.50 ms: 1.05x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 32.2 ns: 1.04x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 67.2 ms: 1.03x faster                                                 |
| bench_mp_pool           | 43.2 ms                                                | 42.1 ms: 1.03x faster                                                 |
| nbody                   | 65.5 ms                                                | 65.2 ms: 1.00x faster                                                 |
| hexiom                  | 4.73 ms                                                | 4.74 ms: 1.00x slower                                                 |
| logging_simple          | 3.50 us                                                | 3.51 us: 1.00x slower                                                 |
| mako                    | 8.49 ms                                                | 8.53 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                 |
| chaos                   | 49.5 ms                                                | 49.8 ms: 1.01x slower                                                 |
| async_generators        | 195 ms                                                 | 197 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.25 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| logging_format          | 3.78 us                                                | 3.83 us: 1.01x slower                                                 |
| scimark_fft             | 199 ms                                                 | 202 ms: 1.02x slower                                                  |
| regex_compile           | 76.7 ms                                                | 78.4 ms: 1.02x slower                                                 |
| xml_etree_generate      | 48.8 ms                                                | 49.9 ms: 1.02x slower                                                 |
| mdp                     | 1.54 sec                                               | 1.58 sec: 1.02x slower                                                |
| json_dumps              | 7.72 ms                                                | 7.91 ms: 1.02x slower                                                 |
| sympy_sum               | 86.0 ms                                                | 88.7 ms: 1.03x slower                                                 |
| dulwich_log             | 29.9 ms                                                | 30.8 ms: 1.03x slower                                                 |
| fannkuch                | 261 ms                                                 | 269 ms: 1.03x slower                                                  |
| pickle                  | 7.17 us                                                | 7.42 us: 1.04x slower                                                 |
| pylint                  | 271 ms                                                 | 280 ms: 1.04x slower                                                  |
| coroutines              | 17.7 ms                                                | 18.5 ms: 1.04x slower                                                 |
| json_loads              | 16.1 us                                                | 16.8 us: 1.04x slower                                                 |
| scimark_sor             | 83.0 ms                                                | 86.7 ms: 1.04x slower                                                 |
| unpickle                | 9.70 us                                                | 10.1 us: 1.04x slower                                                 |
| telco                   | 3.39 ms                                                | 3.56 ms: 1.05x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 180 ms: 1.05x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 12.1 ms: 1.05x slower                                                 |
| spectral_norm           | 72.8 ms                                                | 76.7 ms: 1.05x slower                                                 |
| async_tree_none         | 285 ms                                                 | 301 ms: 1.06x slower                                                  |
| genshi_text             | 15.3 ms                                                | 16.1 ms: 1.06x slower                                                 |
| docutils                | 1.47 sec                                               | 1.56 sec: 1.06x slower                                                |
| bench_thread_pool       | 473 us                                                 | 501 us: 1.06x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 27.9 us: 1.06x slower                                                 |
| xml_etree_process       | 35.2 ms                                                | 37.5 ms: 1.06x slower                                                 |
| html5lib                | 34.7 ms                                                | 36.9 ms: 1.06x slower                                                 |
| sympy_str               | 152 ms                                                 | 161 ms: 1.07x slower                                                  |
| float                   | 53.0 ms                                                | 56.5 ms: 1.07x slower                                                 |
| deepcopy                | 224 us                                                 | 240 us: 1.07x slower                                                  |
| regex_dna               | 152 ms                                                 | 163 ms: 1.07x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.06 us: 1.08x slower                                                 |
| sympy_expand            | 243 ms                                                 | 262 ms: 1.08x slower                                                  |
| pprint_safe_repr        | 465 ms                                                 | 503 ms: 1.08x slower                                                  |
| pprint_pformat          | 950 ms                                                 | 1.03 sec: 1.08x slower                                                |
| async_tree_cpu_io_mixed | 534 ms                                                 | 580 ms: 1.08x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 32.4 ms: 1.09x slower                                                 |
| go                      | 109 ms                                                 | 119 ms: 1.09x slower                                                  |
| thrift                  | 433 us                                                 | 474 us: 1.09x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.39 us: 1.09x slower                                                 |
| pycparser               | 697 ms                                                 | 762 ms: 1.09x slower                                                  |
| json                    | 2.77 ms                                                | 3.04 ms: 1.10x slower                                                 |
| scimark_lu              | 72.1 ms                                                | 78.9 ms: 1.10x slower                                                 |
| raytrace                | 207 ms                                                 | 228 ms: 1.10x slower                                                  |
| tornado_http            | 72.4 ms                                                | 79.7 ms: 1.10x slower                                                 |
| django_template         | 21.0 ms                                                | 23.1 ms: 1.10x slower                                                 |
| python_startup          | 11.5 ms                                                | 12.7 ms: 1.10x slower                                                 |
| sqlglot_optimize        | 31.2 ms                                                | 34.5 ms: 1.11x slower                                                 |
| regex_v8                | 16.2 ms                                                | 18.0 ms: 1.11x slower                                                 |
| deltablue               | 2.81 ms                                                | 3.12 ms: 1.11x slower                                                 |
| scimark_monte_carlo     | 46.4 ms                                                | 51.6 ms: 1.11x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 177 us: 1.11x slower                                                  |
| pyflate                 | 311 ms                                                 | 347 ms: 1.11x slower                                                  |
| chameleon               | 4.57 ms                                                | 5.14 ms: 1.12x slower                                                 |
| pickle_pure_python      | 199 us                                                 | 224 us: 1.12x slower                                                  |
| richards                | 32.2 ms                                                | 36.4 ms: 1.13x slower                                                 |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 59.6 ms: 1.15x slower                                                 |
| flaskblogging           | 2.42 ms                                                | 2.79 ms: 1.15x slower                                                 |
| async_tree_memoization  | 336 ms                                                 | 391 ms: 1.17x slower                                                  |
| async_tree_io           | 706 ms                                                 | 833 ms: 1.18x slower                                                  |
| logging_silent          | 68.0 ns                                                | 81.8 ns: 1.20x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.48 ms: 1.32x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.30 ms: 1.36x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (2): nqueens, meteor_contest
Ignored benchmarks (10) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# Results vs. 3.11.0

- fork: python
- ref: 2e91dba437fe5c56c6f8
- machine: darwin-arm64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.06x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 168 ms: 1.04x slower                                                  |
| chameleon      | 4.57 ms                                                | 5.16 ms: 1.13x slower                                                 |
| docutils       | 1.47 sec                                               | 1.57 sec: 1.07x slower                                                |
| html5lib       | 34.7 ms                                                | 37.0 ms: 1.07x slower                                                 |
| tornado_http   | 72.4 ms                                                | 79.1 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 65.3 ms: 1.00x faster                                                 |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| float          | 53.0 ms                                                | 56.7 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_compile  | 76.7 ms                                                | 78.8 ms: 1.03x slower                                                 |
| regex_dna      | 152 ms                                                 | 159 ms: 1.05x slower                                                  |
| regex_v8       | 16.2 ms                                                | 17.1 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 99.0 ms: 1.07x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.51 us: 1.05x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.82 us: 1.00x slower                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 70.1 ms: 1.01x slower                                                 |
| xml_etree_generate   | 48.8 ms                                                | 50.3 ms: 1.03x slower                                                 |
| json_loads           | 16.1 us                                                | 16.6 us: 1.03x slower                                                 |
| json_dumps           | 7.72 ms                                                | 7.99 ms: 1.03x slower                                                 |
| pickle               | 7.17 us                                                | 7.42 us: 1.04x slower                                                 |
| unpickle             | 9.70 us                                                | 10.1 us: 1.04x slower                                                 |
| xml_etree_process    | 35.2 ms                                                | 37.7 ms: 1.07x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 176 us: 1.11x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 224 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 9.23 ms: 1.01x faster                                                 |
| python_startup         | 11.5 ms                                                | 15.4 ms: 1.34x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.53 ms: 1.01x slower                                                 |
| genshi_text     | 15.3 ms                                                | 16.3 ms: 1.07x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 32.3 ms: 1.08x slower                                                 |
| django_template | 21.0 ms                                                | 22.9 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 58.6 ms                                                | 45.6 ms: 1.29x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 99.0 ms: 1.07x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| generators              | 28.8 ms                                                | 27.1 ms: 1.06x faster                                                 |
| unpickle_list           | 2.63 us                                                | 2.51 us: 1.05x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 32.0 ns: 1.05x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 9.23 ms: 1.01x faster                                                 |
| hexiom                  | 4.73 ms                                                | 4.70 ms: 1.01x faster                                                 |
| nbody                   | 65.5 ms                                                | 65.3 ms: 1.00x faster                                                 |
| meteor_contest          | 73.8 ms                                                | 73.7 ms: 1.00x faster                                                 |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.82 us: 1.00x slower                                                 |
| logging_simple          | 3.50 us                                                | 3.52 us: 1.00x slower                                                 |
| mako                    | 8.49 ms                                                | 8.53 ms: 1.01x slower                                                 |
| create_gc_cycles        | 726 us                                                 | 733 us: 1.01x slower                                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 70.1 ms: 1.01x slower                                                 |
| logging_format          | 3.78 us                                                | 3.83 us: 1.01x slower                                                 |
| scimark_fft             | 199 ms                                                 | 202 ms: 1.01x slower                                                  |
| chaos                   | 49.5 ms                                                | 50.3 ms: 1.02x slower                                                 |
| async_generators        | 195 ms                                                 | 198 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.26 ms: 1.02x slower                                                 |
| mdp                     | 1.54 sec                                               | 1.58 sec: 1.03x slower                                                |
| regex_compile           | 76.7 ms                                                | 78.8 ms: 1.03x slower                                                 |
| xml_etree_generate      | 48.8 ms                                                | 50.3 ms: 1.03x slower                                                 |
| json_loads              | 16.1 us                                                | 16.6 us: 1.03x slower                                                 |
| json_dumps              | 7.72 ms                                                | 7.99 ms: 1.03x slower                                                 |
| pickle                  | 7.17 us                                                | 7.42 us: 1.04x slower                                                 |
| fannkuch                | 261 ms                                                 | 270 ms: 1.04x slower                                                  |
| scimark_sor             | 83.0 ms                                                | 86.2 ms: 1.04x slower                                                 |
| sympy_sum               | 86.0 ms                                                | 89.6 ms: 1.04x slower                                                 |
| unpickle                | 9.70 us                                                | 10.1 us: 1.04x slower                                                 |
| 2to3                    | 161 ms                                                 | 168 ms: 1.04x slower                                                  |
| coroutines              | 17.7 ms                                                | 18.6 ms: 1.05x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 179 ms: 1.05x slower                                                  |
| regex_dna               | 152 ms                                                 | 159 ms: 1.05x slower                                                  |
| flaskblogging           | 2.42 ms                                                | 2.54 ms: 1.05x slower                                                 |
| telco                   | 3.39 ms                                                | 3.57 ms: 1.05x slower                                                 |
| spectral_norm           | 72.8 ms                                                | 76.8 ms: 1.06x slower                                                 |
| regex_v8                | 16.2 ms                                                | 17.1 ms: 1.06x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 12.1 ms: 1.06x slower                                                 |
| pylint                  | 271 ms                                                 | 287 ms: 1.06x slower                                                  |
| sympy_str               | 152 ms                                                 | 162 ms: 1.07x slower                                                  |
| genshi_text             | 15.3 ms                                                | 16.3 ms: 1.07x slower                                                 |
| docutils                | 1.47 sec                                               | 1.57 sec: 1.07x slower                                                |
| dulwich_log             | 29.9 ms                                                | 31.8 ms: 1.07x slower                                                 |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.80 ms: 1.07x slower                                                 |
| html5lib                | 34.7 ms                                                | 37.0 ms: 1.07x slower                                                 |
| deepcopy_reduce         | 1.91 us                                                | 2.04 us: 1.07x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 28.1 us: 1.07x slower                                                 |
| xml_etree_process       | 35.2 ms                                                | 37.7 ms: 1.07x slower                                                 |
| float                   | 53.0 ms                                                | 56.7 ms: 1.07x slower                                                 |
| async_tree_none         | 285 ms                                                 | 305 ms: 1.07x slower                                                  |
| deepcopy                | 224 us                                                 | 240 us: 1.07x slower                                                  |
| sympy_expand            | 243 ms                                                 | 261 ms: 1.07x slower                                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 67.3 ms: 1.07x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.37 us: 1.08x slower                                                 |
| json                    | 2.77 ms                                                | 2.99 ms: 1.08x slower                                                 |
| thrift                  | 433 us                                                 | 470 us: 1.08x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 32.3 ms: 1.08x slower                                                 |
| pprint_safe_repr        | 465 ms                                                 | 505 ms: 1.09x slower                                                  |
| django_template         | 21.0 ms                                                | 22.9 ms: 1.09x slower                                                 |
| pprint_pformat          | 950 ms                                                 | 1.03 sec: 1.09x slower                                                |
| pycparser               | 697 ms                                                 | 759 ms: 1.09x slower                                                  |
| scimark_lu              | 72.1 ms                                                | 78.6 ms: 1.09x slower                                                 |
| go                      | 109 ms                                                 | 119 ms: 1.09x slower                                                  |
| tornado_http            | 72.4 ms                                                | 79.1 ms: 1.09x slower                                                 |
| bench_thread_pool       | 473 us                                                 | 517 us: 1.09x slower                                                  |
| raytrace                | 207 ms                                                 | 227 ms: 1.10x slower                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 587 ms: 1.10x slower                                                  |
| deltablue               | 2.81 ms                                                | 3.10 ms: 1.10x slower                                                 |
| sqlglot_optimize        | 31.2 ms                                                | 34.4 ms: 1.10x slower                                                 |
| scimark_monte_carlo     | 46.4 ms                                                | 51.4 ms: 1.11x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 176 us: 1.11x slower                                                  |
| pyflate                 | 311 ms                                                 | 346 ms: 1.11x slower                                                  |
| comprehensions          | 16.1 us                                                | 18.0 us: 1.12x slower                                                 |
| richards                | 32.2 ms                                                | 36.2 ms: 1.13x slower                                                 |
| pickle_pure_python      | 199 us                                                 | 224 us: 1.13x slower                                                  |
| chameleon               | 4.57 ms                                                | 5.16 ms: 1.13x slower                                                 |
| dask                    | 226 ms                                                 | 258 ms: 1.14x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 59.7 ms: 1.15x slower                                                 |
| async_tree_memoization  | 336 ms                                                 | 400 ms: 1.19x slower                                                  |
| logging_silent          | 68.0 ns                                                | 81.6 ns: 1.20x slower                                                 |
| async_tree_io           | 706 ms                                                 | 855 ms: 1.21x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.47 ms: 1.31x slower                                                 |
| python_startup          | 11.5 ms                                                | 15.4 ms: 1.34x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.29 ms: 1.35x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (5): nqueens, pathlib, gc_traversal, pickle_dict, bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, gunicorn, mypy2

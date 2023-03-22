
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: bb396ee
- commit date: 2023-03-11
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 166 ms: 1.03x slower                                   |
| chameleon      | 4.57 ms                                                | 4.51 ms: 1.01x faster                                  |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.02x slower                                 |
| html5lib       | 34.7 ms                                                | 35.8 ms: 1.03x slower                                  |
| tornado_http   | 72.4 ms                                                | 68.7 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 64.1 ms: 1.02x faster                                  |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                   |
| float          | 53.0 ms                                                | 53.6 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.7 ms: 1.01x faster                                  |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                  |
| regex_dna      | 152 ms                                                 | 152 ms: 1.00x slower                                   |
| regex_effbot   | 2.63 ms                                                | 2.69 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.30 ms: 1.23x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 97.2 ms: 1.09x faster                                  |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.09x faster                                   |
| pickle_pure_python   | 199 us                                                 | 190 us: 1.04x faster                                   |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| unpickle_list        | 2.63 us                                                | 2.69 us: 1.02x slower                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 70.8 ms: 1.02x slower                                  |
| pickle               | 7.17 us                                                | 7.48 us: 1.04x slower                                  |
| xml_etree_process    | 35.2 ms                                                | 36.8 ms: 1.04x slower                                  |
| xml_etree_generate   | 48.8 ms                                                | 51.0 ms: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 8.93 ms: 1.04x faster                                  |
| python_startup         | 11.5 ms                                                | 11.1 ms: 1.04x faster                                  |
| Geometric mean         | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.47 ms: 1.14x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.9 ms: 1.03x faster                                  |
| genshi_xml      | 29.8 ms                                                | 29.4 ms: 1.02x faster                                  |
| django_template | 21.0 ms                                                | 21.7 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-darwin-arm64-python-main-3.12.0a6+-bb396ee |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 414 ms: 1.57x faster                                   |
| json_dumps              | 7.72 ms                                                | 6.30 ms: 1.23x faster                                  |
| mako                    | 8.49 ms                                                | 7.47 ms: 1.14x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 97.2 ms: 1.09x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 145 us: 1.09x faster                                   |
| deltablue               | 2.81 ms                                                | 2.59 ms: 1.09x faster                                  |
| hexiom                  | 4.73 ms                                                | 4.45 ms: 1.06x faster                                  |
| tornado_http            | 72.4 ms                                                | 68.7 ms: 1.05x faster                                  |
| richards                | 32.2 ms                                                | 30.7 ms: 1.05x faster                                  |
| pickle_pure_python      | 199 us                                                 | 190 us: 1.04x faster                                   |
| python_startup_no_site  | 9.31 ms                                                | 8.93 ms: 1.04x faster                                  |
| python_startup          | 11.5 ms                                                | 11.1 ms: 1.04x faster                                  |
| chaos                   | 49.5 ms                                                | 47.9 ms: 1.03x faster                                  |
| create_gc_cycles        | 726 us                                                 | 704 us: 1.03x faster                                   |
| mdp                     | 1.54 sec                                               | 1.50 sec: 1.03x faster                                 |
| pycparser               | 697 ms                                                 | 678 ms: 1.03x faster                                   |
| genshi_text             | 15.3 ms                                                | 14.9 ms: 1.03x faster                                  |
| unpack_sequence         | 33.6 ns                                                | 32.8 ns: 1.02x faster                                  |
| nbody                   | 65.5 ms                                                | 64.1 ms: 1.02x faster                                  |
| generators              | 28.8 ms                                                | 28.2 ms: 1.02x faster                                  |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.18 ms: 1.02x faster                                  |
| scimark_fft             | 199 ms                                                 | 196 ms: 1.02x faster                                   |
| genshi_xml              | 29.8 ms                                                | 29.4 ms: 1.02x faster                                  |
| regex_compile           | 76.7 ms                                                | 75.7 ms: 1.01x faster                                  |
| fannkuch                | 261 ms                                                 | 257 ms: 1.01x faster                                   |
| chameleon               | 4.57 ms                                                | 4.51 ms: 1.01x faster                                  |
| pathlib                 | 27.8 ms                                                | 27.5 ms: 1.01x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.17 ms: 1.01x faster                                  |
| dulwich_log             | 29.9 ms                                                | 29.6 ms: 1.01x faster                                  |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                  |
| gc_traversal            | 2.43 ms                                                | 2.43 ms: 1.00x faster                                  |
| regex_dna               | 152 ms                                                 | 152 ms: 1.00x slower                                   |
| telco                   | 3.39 ms                                                | 3.40 ms: 1.00x slower                                  |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                   |
| deepcopy                | 224 us                                                 | 225 us: 1.01x slower                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| float                   | 53.0 ms                                                | 53.6 ms: 1.01x slower                                  |
| logging_silent          | 68.0 ns                                                | 68.9 ns: 1.01x slower                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.02x slower                                 |
| go                      | 109 ms                                                 | 111 ms: 1.02x slower                                   |
| async_tree_none         | 285 ms                                                 | 290 ms: 1.02x slower                                   |
| coverage                | 58.6 ms                                                | 59.7 ms: 1.02x slower                                  |
| unpickle_list           | 2.63 us                                                | 2.69 us: 1.02x slower                                  |
| coroutines              | 17.7 ms                                                | 18.1 ms: 1.02x slower                                  |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                   |
| sympy_expand            | 243 ms                                                 | 248 ms: 1.02x slower                                   |
| regex_effbot            | 2.63 ms                                                | 2.69 ms: 1.02x slower                                  |
| sympy_str               | 152 ms                                                 | 155 ms: 1.02x slower                                   |
| xml_etree_iterparse     | 69.2 ms                                                | 70.8 ms: 1.02x slower                                  |
| sympy_integrate         | 11.5 ms                                                | 11.8 ms: 1.02x slower                                  |
| json                    | 2.77 ms                                                | 2.84 ms: 1.03x slower                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 64.3 ms: 1.03x slower                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 548 ms: 1.03x slower                                   |
| 2to3                    | 161 ms                                                 | 166 ms: 1.03x slower                                   |
| pprint_pformat          | 950 ms                                                 | 979 ms: 1.03x slower                                   |
| django_template         | 21.0 ms                                                | 21.7 ms: 1.03x slower                                  |
| sympy_sum               | 86.0 ms                                                | 88.7 ms: 1.03x slower                                  |
| spectral_norm           | 72.8 ms                                                | 75.0 ms: 1.03x slower                                  |
| sqlglot_optimize        | 31.2 ms                                                | 32.2 ms: 1.03x slower                                  |
| html5lib                | 34.7 ms                                                | 35.8 ms: 1.03x slower                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.97 us: 1.03x slower                                  |
| pprint_safe_repr        | 465 ms                                                 | 481 ms: 1.04x slower                                   |
| crypto_pyaes            | 51.7 ms                                                | 53.7 ms: 1.04x slower                                  |
| logging_simple          | 3.50 us                                                | 3.64 us: 1.04x slower                                  |
| scimark_lu              | 72.1 ms                                                | 75.0 ms: 1.04x slower                                  |
| logging_format          | 3.78 us                                                | 3.94 us: 1.04x slower                                  |
| pickle                  | 7.17 us                                                | 7.48 us: 1.04x slower                                  |
| xml_etree_process       | 35.2 ms                                                | 36.8 ms: 1.04x slower                                  |
| thrift                  | 433 us                                                 | 453 us: 1.04x slower                                   |
| xml_etree_generate      | 48.8 ms                                                | 51.0 ms: 1.05x slower                                  |
| bench_mp_pool           | 43.2 ms                                                | 45.2 ms: 1.05x slower                                  |
| async_tree_io           | 706 ms                                                 | 745 ms: 1.05x slower                                   |
| scimark_sor             | 83.0 ms                                                | 88.4 ms: 1.06x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                  |
| pyflate                 | 311 ms                                                 | 332 ms: 1.07x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.23 ms: 1.10x slower                                  |
| raytrace                | 207 ms                                                 | 228 ms: 1.10x slower                                   |
| sqlglot_parse           | 957 us                                                 | 1.06 ms: 1.10x slower                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 51.3 ms: 1.11x slower                                  |
| comprehensions          | 16.1 us                                                | 17.9 us: 1.12x slower                                  |
| async_generators        | 195 ms                                                 | 267 ms: 1.37x slower                                   |
| dask                    | 226 ms                                                 | 323 ms: 1.43x slower                                   |
| Geometric mean          | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (8): pickle_list, meteor_contest, bench_thread_pool, deepcopy_memo, async_tree_memoization, unpickle, nqueens, mypy2
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint

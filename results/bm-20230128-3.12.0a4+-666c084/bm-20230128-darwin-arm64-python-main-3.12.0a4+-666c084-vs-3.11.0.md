
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 666c084
- commit date: 2023-01-28
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                   |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| html5lib       | 34.7 ms                                                | 35.2 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.7 ms: 1.02x faster                                  |
| nbody          | 65.5 ms                                                | 64.2 ms: 1.02x faster                                  |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 73.6 ms: 1.04x faster                                  |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.65 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.13 ms: 1.26x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 93.9 ms: 1.13x faster                                  |
| unpickle_pure_python | 159 us                                                 | 148 us: 1.07x faster                                   |
| pickle_pure_python   | 199 us                                                 | 192 us: 1.03x faster                                   |
| xml_etree_iterparse  | 69.2 ms                                                | 67.9 ms: 1.02x faster                                  |
| xml_etree_generate   | 48.8 ms                                                | 49.4 ms: 1.01x slower                                  |
| xml_etree_process    | 35.2 ms                                                | 35.8 ms: 1.02x slower                                  |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                  |
| json_loads           | 16.1 us                                                | 16.4 us: 1.02x slower                                  |
| unpickle_list        | 2.63 us                                                | 2.73 us: 1.04x slower                                  |
| unpickle             | 9.70 us                                                | 10.1 us: 1.05x slower                                  |
| pickle               | 7.17 us                                                | 7.52 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.39 ms: 1.26x faster                                  |
| python_startup         | 11.5 ms                                                | 9.40 ms: 1.23x faster                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.25 ms: 1.17x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.7 ms: 1.04x faster                                  |
| genshi_xml      | 29.8 ms                                                | 29.0 ms: 1.03x faster                                  |
| django_template | 21.0 ms                                                | 21.3 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 422 ms: 1.55x faster                                   |
| pathlib                 | 27.8 ms                                                | 20.6 ms: 1.35x faster                                  |
| json_dumps              | 7.72 ms                                                | 6.13 ms: 1.26x faster                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.39 ms: 1.26x faster                                  |
| python_startup          | 11.5 ms                                                | 9.40 ms: 1.23x faster                                  |
| mako                    | 8.49 ms                                                | 7.25 ms: 1.17x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.79 ms: 1.15x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 93.9 ms: 1.13x faster                                  |
| deltablue               | 2.81 ms                                                | 2.50 ms: 1.12x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 148 us: 1.07x faster                                   |
| scimark_sor             | 83.0 ms                                                | 77.8 ms: 1.07x faster                                  |
| create_gc_cycles        | 726 us                                                 | 688 us: 1.06x faster                                   |
| sympy_sum               | 86.0 ms                                                | 81.9 ms: 1.05x faster                                  |
| bench_thread_pool       | 473 us                                                 | 450 us: 1.05x faster                                   |
| dulwich_log             | 29.9 ms                                                | 28.5 ms: 1.05x faster                                  |
| sympy_str               | 152 ms                                                 | 145 ms: 1.05x faster                                   |
| regex_compile           | 76.7 ms                                                | 73.6 ms: 1.04x faster                                  |
| async_tree_memoization  | 336 ms                                                 | 323 ms: 1.04x faster                                   |
| scimark_fft             | 199 ms                                                 | 192 ms: 1.04x faster                                   |
| richards                | 32.2 ms                                                | 31.0 ms: 1.04x faster                                  |
| genshi_text             | 15.3 ms                                                | 14.7 ms: 1.04x faster                                  |
| chaos                   | 49.5 ms                                                | 47.7 ms: 1.04x faster                                  |
| pickle_pure_python      | 199 us                                                 | 192 us: 1.03x faster                                   |
| nqueens                 | 61.8 ms                                                | 59.9 ms: 1.03x faster                                  |
| sympy_integrate         | 11.5 ms                                                | 11.1 ms: 1.03x faster                                  |
| genshi_xml              | 29.8 ms                                                | 29.0 ms: 1.03x faster                                  |
| coverage                | 58.6 ms                                                | 57.1 ms: 1.03x faster                                  |
| float                   | 53.0 ms                                                | 51.7 ms: 1.02x faster                                  |
| logging_silent          | 68.0 ns                                                | 66.4 ns: 1.02x faster                                  |
| pycparser               | 697 ms                                                 | 680 ms: 1.02x faster                                   |
| unpack_sequence         | 33.6 ns                                                | 32.8 ns: 1.02x faster                                  |
| deepcopy                | 224 us                                                 | 219 us: 1.02x faster                                   |
| mdp                     | 1.54 sec                                               | 1.51 sec: 1.02x faster                                 |
| nbody                   | 65.5 ms                                                | 64.2 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 67.9 ms: 1.02x faster                                  |
| scimark_lu              | 72.1 ms                                                | 70.7 ms: 1.02x faster                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.88 us: 1.01x faster                                  |
| sympy_expand            | 243 ms                                                 | 240 ms: 1.01x faster                                   |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| regex_dna               | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| fannkuch                | 261 ms                                                 | 258 ms: 1.01x faster                                   |
| deepcopy_memo           | 26.3 us                                                | 26.0 us: 1.01x faster                                  |
| gc_traversal            | 2.43 ms                                                | 2.41 ms: 1.01x faster                                  |
| spectral_norm           | 72.8 ms                                                | 72.3 ms: 1.01x faster                                  |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                  |
| hexiom                  | 4.73 ms                                                | 4.70 ms: 1.01x faster                                  |
| meteor_contest          | 73.8 ms                                                | 73.8 ms: 1.00x faster                                  |
| logging_format          | 3.78 us                                                | 3.79 us: 1.00x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 51.9 ms: 1.00x slower                                  |
| raytrace                | 207 ms                                                 | 208 ms: 1.00x slower                                   |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.01x slower                                   |
| regex_effbot            | 2.63 ms                                                | 2.65 ms: 1.01x slower                                  |
| pprint_safe_repr        | 465 ms                                                 | 468 ms: 1.01x slower                                   |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                   |
| sqlglot_optimize        | 31.2 ms                                                | 31.4 ms: 1.01x slower                                  |
| telco                   | 3.39 ms                                                | 3.43 ms: 1.01x slower                                  |
| async_tree_none         | 285 ms                                                 | 288 ms: 1.01x slower                                   |
| django_template         | 21.0 ms                                                | 21.3 ms: 1.01x slower                                  |
| xml_etree_generate      | 48.8 ms                                                | 49.4 ms: 1.01x slower                                  |
| xml_etree_process       | 35.2 ms                                                | 35.8 ms: 1.02x slower                                  |
| html5lib                | 34.7 ms                                                | 35.2 ms: 1.02x slower                                  |
| go                      | 109 ms                                                 | 111 ms: 1.02x slower                                   |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 544 ms: 1.02x slower                                   |
| json_loads              | 16.1 us                                                | 16.4 us: 1.02x slower                                  |
| async_generators        | 195 ms                                                 | 200 ms: 1.02x slower                                   |
| json                    | 2.77 ms                                                | 2.86 ms: 1.03x slower                                  |
| thrift                  | 433 us                                                 | 449 us: 1.04x slower                                   |
| unpickle_list           | 2.63 us                                                | 2.73 us: 1.04x slower                                  |
| pyflate                 | 311 ms                                                 | 324 ms: 1.04x slower                                   |
| unpickle                | 9.70 us                                                | 10.1 us: 1.05x slower                                  |
| async_tree_io           | 706 ms                                                 | 740 ms: 1.05x slower                                   |
| pickle                  | 7.17 us                                                | 7.52 us: 1.05x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.05x slower                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 48.9 ms: 1.05x slower                                  |
| sqlglot_parse           | 957 us                                                 | 1.02 ms: 1.06x slower                                  |
| coroutines              | 17.7 ms                                                | 18.8 ms: 1.06x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                  |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                   |
| generators              | 28.8 ms                                                | 34.7 ms: 1.20x slower                                  |
| dask                    | 226 ms                                                 | 319 ms: 1.41x slower                                   |
| Geometric mean          | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (6): tornado_http, bench_mp_pool, pickle_dict, pprint_pformat, logging_simple, chameleon
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230128-3.12.0a4+-666c084/bm-20230128-darwin-arm64-python-main-3.12.0a4+-666c084.json: mypy

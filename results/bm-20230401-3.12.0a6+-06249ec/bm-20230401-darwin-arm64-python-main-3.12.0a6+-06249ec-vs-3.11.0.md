
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 168 ms: 1.04x slower                                   |
| chameleon      | 4.60 ms                                                | 4.50 ms: 1.02x faster                                  |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.02x slower                                 |
| html5lib       | 34.7 ms                                                | 36.8 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 60.4 ms: 1.09x faster                                  |
| pidigits       | 281 ms                                                 | 280 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 16.1 ms: 1.00x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.70 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.23 ms: 1.22x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 99.1 ms: 1.09x faster                                  |
| unpickle_pure_python | 159 us                                                 | 148 us: 1.07x faster                                   |
| pickle_pure_python   | 201 us                                                 | 193 us: 1.04x faster                                   |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| unpickle_list        | 2.65 us                                                | 2.69 us: 1.02x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 71.3 ms: 1.02x slower                                  |
| pickle_list          | 2.81 us                                                | 2.91 us: 1.03x slower                                  |
| pickle               | 7.15 us                                                | 7.47 us: 1.05x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 36.8 ms: 1.05x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 51.3 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 10.2 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.40 ms: 1.15x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.8 ms: 1.03x faster                                  |
| genshi_xml      | 29.8 ms                                                | 29.4 ms: 1.02x faster                                  |
| django_template | 21.0 ms                                                | 21.8 ms: 1.04x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 439 ms: 1.48x faster                                   |
| json_dumps              | 7.63 ms                                                | 6.23 ms: 1.22x faster                                  |
| mako                    | 8.53 ms                                                | 7.40 ms: 1.15x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.83 ms: 1.13x faster                                  |
| xml_etree_parse         | 108 ms                                                 | 99.1 ms: 1.09x faster                                  |
| nbody                   | 65.6 ms                                                | 60.4 ms: 1.09x faster                                  |
| deltablue               | 2.81 ms                                                | 2.61 ms: 1.08x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 148 us: 1.07x faster                                   |
| hexiom                  | 4.72 ms                                                | 4.43 ms: 1.06x faster                                  |
| scimark_fft             | 200 ms                                                 | 188 ms: 1.06x faster                                   |
| generators              | 28.8 ms                                                | 27.6 ms: 1.04x faster                                  |
| chaos                   | 49.4 ms                                                | 47.5 ms: 1.04x faster                                  |
| unpack_sequence         | 34.1 ns                                                | 32.9 ns: 1.04x faster                                  |
| pickle_pure_python      | 201 us                                                 | 193 us: 1.04x faster                                   |
| genshi_text             | 15.3 ms                                                | 14.8 ms: 1.03x faster                                  |
| richards                | 32.2 ms                                                | 31.4 ms: 1.03x faster                                  |
| scimark_lu              | 73.3 ms                                                | 71.4 ms: 1.03x faster                                  |
| pycparser               | 698 ms                                                 | 680 ms: 1.03x faster                                   |
| chameleon               | 4.60 ms                                                | 4.50 ms: 1.02x faster                                  |
| create_gc_cycles        | 716 us                                                 | 701 us: 1.02x faster                                   |
| logging_silent          | 68.1 ns                                                | 66.8 ns: 1.02x faster                                  |
| genshi_xml              | 29.8 ms                                                | 29.4 ms: 1.02x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 26.0 us: 1.01x faster                                  |
| dulwich_log             | 30.3 ms                                                | 30.0 ms: 1.01x faster                                  |
| meteor_contest          | 73.5 ms                                                | 72.7 ms: 1.01x faster                                  |
| mdp                     | 1.55 sec                                               | 1.54 sec: 1.01x faster                                 |
| deepcopy                | 223 us                                                 | 222 us: 1.01x faster                                   |
| bench_thread_pool       | 474 us                                                 | 472 us: 1.00x faster                                   |
| regex_v8                | 16.1 ms                                                | 16.1 ms: 1.00x faster                                  |
| pidigits                | 281 ms                                                 | 280 ms: 1.00x faster                                   |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                  |
| python_startup_no_site  | 10.2 ms                                                | 10.2 ms: 1.01x slower                                  |
| spectral_norm           | 72.6 ms                                                | 73.1 ms: 1.01x slower                                  |
| json                    | 2.78 ms                                                | 2.80 ms: 1.01x slower                                  |
| async_tree_none         | 286 ms                                                 | 289 ms: 1.01x slower                                   |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.02x slower                                 |
| unpickle_list           | 2.65 us                                                | 2.69 us: 1.02x slower                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 71.3 ms: 1.02x slower                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.34 ms: 1.02x slower                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.95 us: 1.02x slower                                  |
| pprint_pformat          | 954 ms                                                 | 973 ms: 1.02x slower                                   |
| async_tree_cpu_io_mixed | 533 ms                                                 | 545 ms: 1.02x slower                                   |
| pprint_safe_repr        | 466 ms                                                 | 477 ms: 1.02x slower                                   |
| sympy_integrate         | 11.5 ms                                                | 11.8 ms: 1.02x slower                                  |
| regex_effbot            | 2.63 ms                                                | 2.70 ms: 1.03x slower                                  |
| sqlglot_normalize       | 171 ms                                                 | 176 ms: 1.03x slower                                   |
| sqlalchemy_declarative  | 62.6 ms                                                | 64.4 ms: 1.03x slower                                  |
| sympy_str               | 151 ms                                                 | 156 ms: 1.03x slower                                   |
| sympy_expand            | 242 ms                                                 | 250 ms: 1.03x slower                                   |
| pickle_list             | 2.81 us                                                | 2.91 us: 1.03x slower                                  |
| fannkuch                | 261 ms                                                 | 271 ms: 1.04x slower                                   |
| django_template         | 21.0 ms                                                | 21.8 ms: 1.04x slower                                  |
| coverage                | 58.4 ms                                                | 60.5 ms: 1.04x slower                                  |
| logging_simple          | 3.55 us                                                | 3.68 us: 1.04x slower                                  |
| sympy_sum               | 85.5 ms                                                | 88.8 ms: 1.04x slower                                  |
| sqlglot_optimize        | 31.1 ms                                                | 32.3 ms: 1.04x slower                                  |
| telco                   | 3.41 ms                                                | 3.54 ms: 1.04x slower                                  |
| 2to3                    | 161 ms                                                 | 168 ms: 1.04x slower                                   |
| pickle                  | 7.15 us                                                | 7.47 us: 1.05x slower                                  |
| async_tree_io           | 704 ms                                                 | 739 ms: 1.05x slower                                   |
| xml_etree_process       | 35.1 ms                                                | 36.8 ms: 1.05x slower                                  |
| logging_format          | 3.78 us                                                | 3.97 us: 1.05x slower                                  |
| thrift                  | 442 us                                                 | 464 us: 1.05x slower                                   |
| bench_mp_pool           | 43.9 ms                                                | 46.4 ms: 1.06x slower                                  |
| html5lib                | 34.7 ms                                                | 36.8 ms: 1.06x slower                                  |
| nqueens                 | 59.8 ms                                                | 63.3 ms: 1.06x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 54.9 ms: 1.06x slower                                  |
| coroutines              | 17.8 ms                                                | 18.9 ms: 1.06x slower                                  |
| xml_etree_generate      | 48.3 ms                                                | 51.3 ms: 1.06x slower                                  |
| go                      | 109 ms                                                 | 116 ms: 1.07x slower                                   |
| scimark_sor             | 82.6 ms                                                | 88.3 ms: 1.07x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                  |
| raytrace                | 207 ms                                                 | 222 ms: 1.07x slower                                   |
| comprehensions          | 16.1 us                                                | 17.8 us: 1.10x slower                                  |
| pyflate                 | 310 ms                                                 | 343 ms: 1.11x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.25 ms: 1.11x slower                                  |
| sqlglot_parse           | 959 us                                                 | 1.07 ms: 1.12x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 53.0 ms: 1.14x slower                                  |
| async_generators        | 196 ms                                                 | 265 ms: 1.35x slower                                   |
| mypy2                   | 195 ms                                                 | 264 ms: 1.35x slower                                   |
| Geometric mean          | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (9): tornado_http, async_tree_memoization, python_startup, unpickle, pickle_dict, regex_compile, regex_dna, float, pathlib
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230401-3.12.0a6+-06249ec/bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec.json: dask


# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

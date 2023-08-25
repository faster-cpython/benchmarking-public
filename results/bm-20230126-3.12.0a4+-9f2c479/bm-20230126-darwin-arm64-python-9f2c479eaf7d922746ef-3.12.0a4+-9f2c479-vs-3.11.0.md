
# Results vs. 3.11.0

- fork: python
- ref: 9f2c479eaf7d922746ef
- machine: darwin-arm64
- commit hash: 9f2c479
- commit date: 2023-01-26
- overall geometric mean: 1.02x faster \*
- HPT reliability: 97.56%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.14x slower                                                   |
| chameleon      | 4.60 ms                                                | 4.52 ms: 1.02x faster                                                  |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.8 ms: 1.02x faster                                                  |
| nbody          | 65.6 ms                                                | 64.5 ms: 1.02x faster                                                  |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 73.7 ms: 1.04x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| regex_dna      | 152 ms                                                 | 153 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.23 ms: 1.22x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 93.7 ms: 1.15x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 147 us: 1.08x faster                                                   |
| pickle_pure_python   | 201 us                                                 | 194 us: 1.04x faster                                                   |
| xml_etree_iterparse  | 70.1 ms                                                | 67.7 ms: 1.04x faster                                                  |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                                  |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                  |
| xml_etree_process    | 35.1 ms                                                | 35.6 ms: 1.02x slower                                                  |
| xml_etree_generate   | 48.3 ms                                                | 49.3 ms: 1.02x slower                                                  |
| unpickle             | 9.67 us                                                | 9.89 us: 1.02x slower                                                  |
| unpickle_list        | 2.65 us                                                | 2.77 us: 1.05x slower                                                  |
| pickle               | 7.15 us                                                | 7.56 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.39 ms: 1.38x faster                                                  |
| python_startup         | 12.4 ms                                                | 9.40 ms: 1.32x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.27 ms: 1.17x faster                                                  |
| genshi_text     | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 28.9 ms: 1.03x faster                                                  |
| django_template | 21.0 ms                                                | 21.3 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 446 ms: 1.46x faster                                                   |
| python_startup_no_site  | 10.2 ms                                                | 7.39 ms: 1.38x faster                                                  |
| python_startup          | 12.4 ms                                                | 9.40 ms: 1.32x faster                                                  |
| pathlib                 | 27.2 ms                                                | 20.7 ms: 1.31x faster                                                  |
| json_dumps              | 7.63 ms                                                | 6.23 ms: 1.22x faster                                                  |
| mako                    | 8.53 ms                                                | 7.27 ms: 1.17x faster                                                  |
| xml_etree_parse         | 108 ms                                                 | 93.7 ms: 1.15x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.82 ms: 1.13x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.50 ms: 1.13x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 147 us: 1.08x faster                                                   |
| dulwich_log             | 30.3 ms                                                | 28.5 ms: 1.06x faster                                                  |
| bench_thread_pool       | 474 us                                                 | 450 us: 1.05x faster                                                   |
| scimark_sor             | 82.6 ms                                                | 78.3 ms: 1.05x faster                                                  |
| sympy_sum               | 85.5 ms                                                | 81.4 ms: 1.05x faster                                                  |
| sympy_str               | 151 ms                                                 | 145 ms: 1.05x faster                                                   |
| unpack_sequence         | 34.1 ns                                                | 32.7 ns: 1.04x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                  |
| regex_compile           | 76.7 ms                                                | 73.7 ms: 1.04x faster                                                  |
| richards                | 32.2 ms                                                | 31.1 ms: 1.04x faster                                                  |
| async_tree_memoization  | 336 ms                                                 | 324 ms: 1.04x faster                                                   |
| pickle_pure_python      | 201 us                                                 | 194 us: 1.04x faster                                                   |
| xml_etree_iterparse     | 70.1 ms                                                | 67.7 ms: 1.04x faster                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.1 ms: 1.04x faster                                                  |
| chaos                   | 49.4 ms                                                | 47.8 ms: 1.03x faster                                                  |
| create_gc_cycles        | 716 us                                                 | 692 us: 1.03x faster                                                   |
| scimark_fft             | 200 ms                                                 | 193 ms: 1.03x faster                                                   |
| scimark_lu              | 73.3 ms                                                | 71.0 ms: 1.03x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 28.9 ms: 1.03x faster                                                  |
| logging_silent          | 68.1 ns                                                | 66.3 ns: 1.03x faster                                                  |
| coverage                | 58.4 ms                                                | 56.9 ms: 1.03x faster                                                  |
| pycparser               | 698 ms                                                 | 680 ms: 1.03x faster                                                   |
| float                   | 53.0 ms                                                | 51.8 ms: 1.02x faster                                                  |
| fannkuch                | 261 ms                                                 | 256 ms: 1.02x faster                                                   |
| mdp                     | 1.55 sec                                               | 1.51 sec: 1.02x faster                                                 |
| deepcopy                | 223 us                                                 | 219 us: 1.02x faster                                                   |
| chameleon               | 4.60 ms                                                | 4.52 ms: 1.02x faster                                                  |
| nbody                   | 65.6 ms                                                | 64.5 ms: 1.02x faster                                                  |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                 |
| deepcopy_memo           | 26.3 us                                                | 26.0 us: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| sympy_expand            | 242 ms                                                 | 240 ms: 1.01x faster                                                   |
| pprint_pformat          | 954 ms                                                 | 946 ms: 1.01x faster                                                   |
| logging_simple          | 3.55 us                                                | 3.53 us: 1.01x faster                                                  |
| spectral_norm           | 72.6 ms                                                | 72.3 ms: 1.00x faster                                                  |
| pprint_safe_repr        | 466 ms                                                 | 465 ms: 1.00x faster                                                   |
| gc_traversal            | 2.42 ms                                                | 2.41 ms: 1.00x faster                                                  |
| hexiom                  | 4.72 ms                                                | 4.73 ms: 1.00x slower                                                  |
| thrift                  | 442 us                                                 | 443 us: 1.00x slower                                                   |
| meteor_contest          | 73.5 ms                                                | 73.8 ms: 1.00x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 51.9 ms: 1.00x slower                                                  |
| regex_dna               | 152 ms                                                 | 153 ms: 1.01x slower                                                   |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                                  |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.01x slower                                                   |
| logging_format          | 3.78 us                                                | 3.80 us: 1.01x slower                                                  |
| async_tree_none         | 286 ms                                                 | 288 ms: 1.01x slower                                                   |
| sqlglot_optimize        | 31.1 ms                                                | 31.4 ms: 1.01x slower                                                  |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                  |
| django_template         | 21.0 ms                                                | 21.3 ms: 1.01x slower                                                  |
| xml_etree_process       | 35.1 ms                                                | 35.6 ms: 1.02x slower                                                  |
| async_generators        | 196 ms                                                 | 199 ms: 1.02x slower                                                   |
| go                      | 109 ms                                                 | 110 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed | 533 ms                                                 | 544 ms: 1.02x slower                                                   |
| xml_etree_generate      | 48.3 ms                                                | 49.3 ms: 1.02x slower                                                  |
| unpickle                | 9.67 us                                                | 9.89 us: 1.02x slower                                                  |
| json                    | 2.78 ms                                                | 2.84 ms: 1.02x slower                                                  |
| pyflate                 | 310 ms                                                 | 324 ms: 1.04x slower                                                   |
| raytrace                | 207 ms                                                 | 216 ms: 1.05x slower                                                   |
| unpickle_list           | 2.65 us                                                | 2.77 us: 1.05x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.05x slower                                                  |
| async_tree_io           | 704 ms                                                 | 742 ms: 1.05x slower                                                   |
| sqlglot_parse           | 959 us                                                 | 1.01 ms: 1.06x slower                                                  |
| pickle                  | 7.15 us                                                | 7.56 us: 1.06x slower                                                  |
| coroutines              | 17.8 ms                                                | 18.8 ms: 1.06x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 50.4 ms: 1.08x slower                                                  |
| 2to3                    | 161 ms                                                 | 185 ms: 1.14x slower                                                   |
| generators              | 28.8 ms                                                | 34.6 ms: 1.20x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (8): bench_mp_pool, tornado_http, telco, pickle_dict, nqueens, regex_v8, deepcopy_reduce, html5lib
Ignored benchmarks (12) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (2) of results/bm-20230126-3.12.0a4+-9f2c479/bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479.json: dask, mypy


# HPT report

- Reliability score: 97.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

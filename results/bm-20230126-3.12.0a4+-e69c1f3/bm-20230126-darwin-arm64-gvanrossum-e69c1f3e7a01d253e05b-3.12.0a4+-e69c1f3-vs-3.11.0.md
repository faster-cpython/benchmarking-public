
# Results vs. 3.11.0

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: darwin-arm64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.02x faster \*
- HPT reliability: 98.25%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 181 ms: 1.12x slower                                                       |
| chameleon      | 4.60 ms                                                | 4.58 ms: 1.01x faster                                                      |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 64.4 ms: 1.02x faster                                                      |
| float          | 53.0 ms                                                | 52.4 ms: 1.01x faster                                                      |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 73.6 ms: 1.04x faster                                                      |
| regex_dna      | 152 ms                                                 | 150 ms: 1.02x faster                                                       |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                      |
| regex_v8       | 16.1 ms                                                | 16.1 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.15 ms: 1.24x faster                                                      |
| xml_etree_parse      | 108 ms                                                 | 94.8 ms: 1.14x faster                                                      |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.10x faster                                                       |
| pickle_pure_python   | 201 us                                                 | 194 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 70.1 ms                                                | 68.3 ms: 1.03x faster                                                      |
| xml_etree_process    | 35.1 ms                                                | 35.4 ms: 1.01x slower                                                      |
| pickle_list          | 2.81 us                                                | 2.84 us: 1.01x slower                                                      |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                                      |
| unpickle             | 9.67 us                                                | 9.87 us: 1.02x slower                                                      |
| xml_etree_generate   | 48.3 ms                                                | 49.3 ms: 1.02x slower                                                      |
| unpickle_list        | 2.65 us                                                | 2.71 us: 1.02x slower                                                      |
| pickle               | 7.15 us                                                | 7.55 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.38 ms: 1.38x faster                                                      |
| python_startup         | 12.4 ms                                                | 9.40 ms: 1.32x faster                                                      |
| Geometric mean         | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.29 ms: 1.17x faster                                                      |
| genshi_text     | 15.3 ms                                                | 14.8 ms: 1.04x faster                                                      |
| genshi_xml      | 29.8 ms                                                | 28.9 ms: 1.03x faster                                                      |
| django_template | 21.0 ms                                                | 21.1 ms: 1.00x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 395 ms: 1.65x faster                                                       |
| python_startup_no_site  | 10.2 ms                                                | 7.38 ms: 1.38x faster                                                      |
| python_startup          | 12.4 ms                                                | 9.40 ms: 1.32x faster                                                      |
| pathlib                 | 27.2 ms                                                | 20.8 ms: 1.31x faster                                                      |
| json_dumps              | 7.63 ms                                                | 6.15 ms: 1.24x faster                                                      |
| mako                    | 8.53 ms                                                | 7.29 ms: 1.17x faster                                                      |
| xml_etree_parse         | 108 ms                                                 | 94.8 ms: 1.14x faster                                                      |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.83 ms: 1.13x faster                                                      |
| unpickle_pure_python    | 159 us                                                 | 145 us: 1.10x faster                                                       |
| deltablue               | 2.81 ms                                                | 2.59 ms: 1.09x faster                                                      |
| dulwich_log             | 30.3 ms                                                | 28.5 ms: 1.06x faster                                                      |
| bench_thread_pool       | 474 us                                                 | 447 us: 1.06x faster                                                       |
| richards                | 32.2 ms                                                | 30.7 ms: 1.05x faster                                                      |
| sympy_str               | 151 ms                                                 | 145 ms: 1.04x faster                                                       |
| regex_compile           | 76.7 ms                                                | 73.6 ms: 1.04x faster                                                      |
| sympy_sum               | 85.5 ms                                                | 82.0 ms: 1.04x faster                                                      |
| scimark_fft             | 200 ms                                                 | 193 ms: 1.04x faster                                                       |
| genshi_text             | 15.3 ms                                                | 14.8 ms: 1.04x faster                                                      |
| bench_mp_pool           | 43.9 ms                                                | 42.5 ms: 1.03x faster                                                      |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.03x faster                                                      |
| pickle_pure_python      | 201 us                                                 | 194 us: 1.03x faster                                                       |
| logging_silent          | 68.1 ns                                                | 66.0 ns: 1.03x faster                                                      |
| genshi_xml              | 29.8 ms                                                | 28.9 ms: 1.03x faster                                                      |
| chaos                   | 49.4 ms                                                | 48.1 ms: 1.03x faster                                                      |
| xml_etree_iterparse     | 70.1 ms                                                | 68.3 ms: 1.03x faster                                                      |
| pycparser               | 698 ms                                                 | 680 ms: 1.03x faster                                                       |
| scimark_lu              | 73.3 ms                                                | 71.5 ms: 1.03x faster                                                      |
| fannkuch                | 261 ms                                                 | 255 ms: 1.02x faster                                                       |
| nbody                   | 65.6 ms                                                | 64.4 ms: 1.02x faster                                                      |
| coverage                | 58.4 ms                                                | 57.4 ms: 1.02x faster                                                      |
| scimark_monte_carlo     | 46.5 ms                                                | 45.7 ms: 1.02x faster                                                      |
| mdp                     | 1.55 sec                                               | 1.52 sec: 1.02x faster                                                     |
| regex_dna               | 152 ms                                                 | 150 ms: 1.02x faster                                                       |
| unpack_sequence         | 34.1 ns                                                | 33.6 ns: 1.02x faster                                                      |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                     |
| deepcopy                | 223 us                                                 | 220 us: 1.01x faster                                                       |
| pprint_pformat          | 954 ms                                                 | 941 ms: 1.01x faster                                                       |
| pprint_safe_repr        | 466 ms                                                 | 462 ms: 1.01x faster                                                       |
| float                   | 53.0 ms                                                | 52.4 ms: 1.01x faster                                                      |
| regex_effbot            | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                      |
| meteor_contest          | 73.5 ms                                                | 73.0 ms: 1.01x faster                                                      |
| deepcopy_memo           | 26.3 us                                                | 26.1 us: 1.01x faster                                                      |
| create_gc_cycles        | 716 us                                                 | 711 us: 1.01x faster                                                       |
| telco                   | 3.41 ms                                                | 3.39 ms: 1.01x faster                                                      |
| sympy_expand            | 242 ms                                                 | 241 ms: 1.01x faster                                                       |
| chameleon               | 4.60 ms                                                | 4.58 ms: 1.01x faster                                                      |
| hexiom                  | 4.72 ms                                                | 4.71 ms: 1.00x faster                                                      |
| regex_v8                | 16.1 ms                                                | 16.1 ms: 1.00x faster                                                      |
| spectral_norm           | 72.6 ms                                                | 72.8 ms: 1.00x slower                                                      |
| go                      | 109 ms                                                 | 109 ms: 1.00x slower                                                       |
| deepcopy_reduce         | 1.91 us                                                | 1.92 us: 1.00x slower                                                      |
| django_template         | 21.0 ms                                                | 21.1 ms: 1.00x slower                                                      |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                                       |
| thrift                  | 442 us                                                 | 444 us: 1.01x slower                                                       |
| crypto_pyaes            | 51.7 ms                                                | 52.1 ms: 1.01x slower                                                      |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                                      |
| async_tree_none         | 286 ms                                                 | 288 ms: 1.01x slower                                                       |
| xml_etree_process       | 35.1 ms                                                | 35.4 ms: 1.01x slower                                                      |
| pickle_list             | 2.81 us                                                | 2.84 us: 1.01x slower                                                      |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                                      |
| raytrace                | 207 ms                                                 | 210 ms: 1.01x slower                                                       |
| logging_simple          | 3.55 us                                                | 3.60 us: 1.01x slower                                                      |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                       |
| unpickle                | 9.67 us                                                | 9.87 us: 1.02x slower                                                      |
| async_generators        | 196 ms                                                 | 200 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 533 ms                                                 | 544 ms: 1.02x slower                                                       |
| sqlglot_optimize        | 31.1 ms                                                | 31.7 ms: 1.02x slower                                                      |
| xml_etree_generate      | 48.3 ms                                                | 49.3 ms: 1.02x slower                                                      |
| json                    | 2.78 ms                                                | 2.84 ms: 1.02x slower                                                      |
| unpickle_list           | 2.65 us                                                | 2.71 us: 1.02x slower                                                      |
| logging_format          | 3.78 us                                                | 3.87 us: 1.02x slower                                                      |
| scimark_sor             | 82.6 ms                                                | 85.2 ms: 1.03x slower                                                      |
| pyflate                 | 310 ms                                                 | 322 ms: 1.04x slower                                                       |
| coroutines              | 17.8 ms                                                | 18.6 ms: 1.05x slower                                                      |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.05x slower                                                      |
| async_tree_io           | 704 ms                                                 | 743 ms: 1.05x slower                                                       |
| pickle                  | 7.15 us                                                | 7.55 us: 1.06x slower                                                      |
| sqlglot_parse           | 959 us                                                 | 1.01 ms: 1.06x slower                                                      |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                                      |
| 2to3                    | 161 ms                                                 | 181 ms: 1.12x slower                                                       |
| generators              | 28.8 ms                                                | 34.4 ms: 1.20x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (5): tornado_http, async_tree_memoization, nqueens, pickle_dict, html5lib
Ignored benchmarks (12) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (2) of results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: dask, mypy


# HPT report

- Reliability score: 98.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

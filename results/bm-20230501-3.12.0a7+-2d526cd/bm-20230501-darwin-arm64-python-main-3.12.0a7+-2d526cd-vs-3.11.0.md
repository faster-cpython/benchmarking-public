
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.04x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 173 ms: 1.07x slower                                   |
| docutils       | 1.47 sec                                               | 1.56 sec: 1.06x slower                                 |
| html5lib       | 34.7 ms                                                | 37.2 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 69.7 ms: 1.06x slower                                  |
| float          | 53.0 ms                                                | 58.1 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| regex_compile  | 76.7 ms                                                | 77.6 ms: 1.01x slower                                  |
| regex_v8       | 16.1 ms                                                | 16.3 ms: 1.01x slower                                  |
| regex_effbot   | 2.63 ms                                                | 2.69 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.84 ms: 1.12x faster                                  |
| unpickle_pure_python | 159 us                                                 | 151 us: 1.05x faster                                   |
| pickle_pure_python   | 201 us                                                 | 194 us: 1.03x faster                                   |
| unpickle             | 9.67 us                                                | 10.2 us: 1.05x slower                                  |
| pickle_dict          | 18.0 us                                                | 19.0 us: 1.06x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 74.2 ms: 1.06x slower                                  |
| pickle               | 7.15 us                                                | 7.83 us: 1.10x slower                                  |
| json_loads           | 16.1 us                                                | 17.7 us: 1.10x slower                                  |
| pickle_list          | 2.81 us                                                | 3.13 us: 1.11x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 39.8 ms: 1.14x slower                                  |
| unpickle_list        | 2.65 us                                                | 3.16 us: 1.19x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 57.7 ms: 1.20x slower                                  |
| Geometric mean       | (ref)                                                  | 1.06x slower                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.5 ms: 1.00x slower                                  |
| python_startup_no_site | 10.2 ms                                                | 10.4 ms: 1.02x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako           | 8.53 ms                                                | 7.80 ms: 1.09x faster                                  |
| genshi_text    | 15.3 ms                                                | 15.0 ms: 1.02x faster                                  |
| genshi_xml     | 29.8 ms                                                | 30.9 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 449 ms: 1.45x faster                                   |
| unpack_sequence         | 34.1 ns                                                | 28.1 ns: 1.22x faster                                  |
| generators              | 28.8 ms                                                | 25.0 ms: 1.15x faster                                  |
| deltablue               | 2.81 ms                                                | 2.47 ms: 1.14x faster                                  |
| json_dumps              | 7.63 ms                                                | 6.84 ms: 1.12x faster                                  |
| mako                    | 8.53 ms                                                | 7.80 ms: 1.09x faster                                  |
| hexiom                  | 4.72 ms                                                | 4.32 ms: 1.09x faster                                  |
| sqlglot_parse           | 959 us                                                 | 897 us: 1.07x faster                                   |
| unpickle_pure_python    | 159 us                                                 | 151 us: 1.05x faster                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.07 ms: 1.05x faster                                  |
| pickle_pure_python      | 201 us                                                 | 194 us: 1.03x faster                                   |
| create_gc_cycles        | 716 us                                                 | 698 us: 1.02x faster                                   |
| genshi_text             | 15.3 ms                                                | 15.0 ms: 1.02x faster                                  |
| chaos                   | 49.4 ms                                                | 48.4 ms: 1.02x faster                                  |
| richards                | 32.2 ms                                                | 31.6 ms: 1.02x faster                                  |
| coverage                | 58.4 ms                                                | 57.4 ms: 1.02x faster                                  |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| async_tree_none         | 286 ms                                                 | 281 ms: 1.02x faster                                   |
| deepcopy_memo           | 26.3 us                                                | 26.2 us: 1.00x faster                                  |
| go                      | 109 ms                                                 | 109 ms: 1.00x slower                                   |
| gc_traversal            | 2.42 ms                                                | 2.42 ms: 1.00x slower                                  |
| python_startup          | 12.4 ms                                                | 12.5 ms: 1.00x slower                                  |
| dulwich_log             | 30.3 ms                                                | 30.5 ms: 1.01x slower                                  |
| async_tree_io           | 704 ms                                                 | 710 ms: 1.01x slower                                   |
| regex_compile           | 76.7 ms                                                | 77.6 ms: 1.01x slower                                  |
| regex_v8                | 16.1 ms                                                | 16.3 ms: 1.01x slower                                  |
| mdp                     | 1.55 sec                                               | 1.57 sec: 1.01x slower                                 |
| coroutines              | 17.8 ms                                                | 18.0 ms: 1.01x slower                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.33 ms: 1.02x slower                                  |
| pathlib                 | 27.2 ms                                                | 27.8 ms: 1.02x slower                                  |
| python_startup_no_site  | 10.2 ms                                                | 10.4 ms: 1.02x slower                                  |
| regex_effbot            | 2.63 ms                                                | 2.69 ms: 1.02x slower                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.27 ms: 1.03x slower                                  |
| scimark_fft             | 200 ms                                                 | 207 ms: 1.03x slower                                   |
| genshi_xml              | 29.8 ms                                                | 30.9 ms: 1.04x slower                                  |
| logging_silent          | 68.1 ns                                                | 70.8 ns: 1.04x slower                                  |
| scimark_sor             | 82.6 ms                                                | 86.0 ms: 1.04x slower                                  |
| logging_simple          | 3.55 us                                                | 3.70 us: 1.04x slower                                  |
| unpickle                | 9.67 us                                                | 10.2 us: 1.05x slower                                  |
| bench_thread_pool       | 474 us                                                 | 498 us: 1.05x slower                                   |
| meteor_contest          | 73.5 ms                                                | 77.4 ms: 1.05x slower                                  |
| logging_format          | 3.78 us                                                | 3.98 us: 1.05x slower                                  |
| scimark_lu              | 73.3 ms                                                | 77.3 ms: 1.05x slower                                  |
| pickle_dict             | 18.0 us                                                | 19.0 us: 1.06x slower                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 74.2 ms: 1.06x slower                                  |
| docutils                | 1.47 sec                                               | 1.56 sec: 1.06x slower                                 |
| nbody                   | 65.6 ms                                                | 69.7 ms: 1.06x slower                                  |
| nqueens                 | 59.8 ms                                                | 63.5 ms: 1.06x slower                                  |
| spectral_norm           | 72.6 ms                                                | 77.2 ms: 1.06x slower                                  |
| fannkuch                | 261 ms                                                 | 278 ms: 1.07x slower                                   |
| 2to3                    | 161 ms                                                 | 173 ms: 1.07x slower                                   |
| deepcopy                | 223 us                                                 | 238 us: 1.07x slower                                   |
| html5lib                | 34.7 ms                                                | 37.2 ms: 1.07x slower                                  |
| pprint_pformat          | 954 ms                                                 | 1.02 sec: 1.07x slower                                 |
| crypto_pyaes            | 51.7 ms                                                | 56.0 ms: 1.08x slower                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 68.0 ms: 1.09x slower                                  |
| json                    | 2.78 ms                                                | 3.02 ms: 1.09x slower                                  |
| pprint_safe_repr        | 466 ms                                                 | 509 ms: 1.09x slower                                   |
| pickle                  | 7.15 us                                                | 7.83 us: 1.10x slower                                  |
| float                   | 53.0 ms                                                | 58.1 ms: 1.10x slower                                  |
| json_loads              | 16.1 us                                                | 17.7 us: 1.10x slower                                  |
| pyflate                 | 310 ms                                                 | 342 ms: 1.10x slower                                   |
| bench_mp_pool           | 43.9 ms                                                | 48.6 ms: 1.11x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 51.5 ms: 1.11x slower                                  |
| pickle_list             | 2.81 us                                                | 3.13 us: 1.11x slower                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.13 us: 1.11x slower                                  |
| comprehensions          | 16.1 us                                                | 18.0 us: 1.12x slower                                  |
| xml_etree_process       | 35.1 ms                                                | 39.8 ms: 1.14x slower                                  |
| sqlglot_normalize       | 171 ms                                                 | 196 ms: 1.15x slower                                   |
| sqlglot_optimize        | 31.1 ms                                                | 35.8 ms: 1.15x slower                                  |
| telco                   | 3.41 ms                                                | 3.92 ms: 1.15x slower                                  |
| thrift                  | 442 us                                                 | 513 us: 1.16x slower                                   |
| unpickle_list           | 2.65 us                                                | 3.16 us: 1.19x slower                                  |
| xml_etree_generate      | 48.3 ms                                                | 57.7 ms: 1.20x slower                                  |
| raytrace                | 207 ms                                                 | 248 ms: 1.20x slower                                   |
| sqlite_synth            | 1.27 us                                                | 1.59 us: 1.25x slower                                  |
| mypy2                   | 195 ms                                                 | 265 ms: 1.36x slower                                   |
| async_generators        | 196 ms                                                 | 311 ms: 1.59x slower                                   |
| Geometric mean          | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (6): tornado_http, async_tree_memoization, pycparser, pidigits, async_tree_cpu_io_mixed, xml_etree_parse
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230501-3.12.0a7+-2d526cd/bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

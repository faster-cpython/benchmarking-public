
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b2
- machine: darwin-arm64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.01x slower \*
- HPT reliability: 74.72%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 162 ms: 1.00x slower                                       |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                     |
| html5lib       | 34.7 ms                                                | 36.0 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 63.7 ms: 1.03x faster                                      |
| float          | 53.0 ms                                                | 55.2 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.40 ms: 1.10x faster                                      |
| regex_dna      | 152 ms                                                 | 150 ms: 1.02x faster                                       |
| regex_compile  | 76.7 ms                                                | 77.9 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 18.0 us                                                | 17.2 us: 1.05x faster                                      |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                       |
| xml_etree_iterparse  | 70.1 ms                                                | 68.8 ms: 1.02x faster                                      |
| pickle_list          | 2.81 us                                                | 2.76 us: 1.02x faster                                      |
| pickle               | 7.15 us                                                | 7.06 us: 1.01x faster                                      |
| xml_etree_process    | 35.1 ms                                                | 34.9 ms: 1.00x faster                                      |
| unpickle_list        | 2.65 us                                                | 2.70 us: 1.02x slower                                      |
| unpickle             | 9.67 us                                                | 9.98 us: 1.03x slower                                      |
| pickle_pure_python   | 201 us                                                 | 217 us: 1.08x slower                                       |
| unpickle_pure_python | 159 us                                                 | 176 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (3): xml_etree_generate, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 10.1 ms: 1.01x faster                                      |
| Geometric mean         | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 8.53 ms                                                | 8.36 ms: 1.02x faster                                      |
| django_template | 21.0 ms                                                | 20.9 ms: 1.01x faster                                      |
| genshi_xml      | 29.8 ms                                                | 30.3 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                | 2.40 ms: 1.10x faster                                      |
| unpack_sequence         | 34.1 ns                                                | 32.4 ns: 1.05x faster                                      |
| scimark_sor             | 82.6 ms                                                | 78.7 ms: 1.05x faster                                      |
| pickle_dict             | 18.0 us                                                | 17.2 us: 1.05x faster                                      |
| logging_silent          | 68.1 ns                                                | 65.3 ns: 1.04x faster                                      |
| generators              | 28.8 ms                                                | 27.7 ms: 1.04x faster                                      |
| sympy_sum               | 85.5 ms                                                | 82.7 ms: 1.03x faster                                      |
| coroutines              | 17.8 ms                                                | 17.3 ms: 1.03x faster                                      |
| nbody                   | 65.6 ms                                                | 63.7 ms: 1.03x faster                                      |
| scimark_lu              | 73.3 ms                                                | 71.3 ms: 1.03x faster                                      |
| xml_etree_parse         | 108 ms                                                 | 105 ms: 1.03x faster                                       |
| nqueens                 | 59.8 ms                                                | 58.5 ms: 1.02x faster                                      |
| go                      | 109 ms                                                 | 106 ms: 1.02x faster                                       |
| logging_simple          | 3.55 us                                                | 3.48 us: 1.02x faster                                      |
| mako                    | 8.53 ms                                                | 8.36 ms: 1.02x faster                                      |
| xml_etree_iterparse     | 70.1 ms                                                | 68.8 ms: 1.02x faster                                      |
| thrift                  | 442 us                                                 | 434 us: 1.02x faster                                       |
| pickle_list             | 2.81 us                                                | 2.76 us: 1.02x faster                                      |
| regex_dna               | 152 ms                                                 | 150 ms: 1.02x faster                                       |
| bench_thread_pool       | 474 us                                                 | 468 us: 1.01x faster                                       |
| pickle                  | 7.15 us                                                | 7.06 us: 1.01x faster                                      |
| sqlalchemy_declarative  | 62.6 ms                                                | 61.9 ms: 1.01x faster                                      |
| raytrace                | 207 ms                                                 | 205 ms: 1.01x faster                                       |
| python_startup_no_site  | 10.2 ms                                                | 10.1 ms: 1.01x faster                                      |
| deltablue               | 2.81 ms                                                | 2.79 ms: 1.01x faster                                      |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                     |
| spectral_norm           | 72.6 ms                                                | 72.1 ms: 1.01x faster                                      |
| sympy_str               | 151 ms                                                 | 150 ms: 1.01x faster                                       |
| django_template         | 21.0 ms                                                | 20.9 ms: 1.01x faster                                      |
| mdp                     | 1.55 sec                                               | 1.54 sec: 1.01x faster                                     |
| fannkuch                | 261 ms                                                 | 260 ms: 1.01x faster                                       |
| xml_etree_process       | 35.1 ms                                                | 34.9 ms: 1.00x faster                                      |
| logging_format          | 3.78 us                                                | 3.76 us: 1.00x faster                                      |
| crypto_pyaes            | 51.7 ms                                                | 51.5 ms: 1.00x faster                                      |
| hexiom                  | 4.72 ms                                                | 4.71 ms: 1.00x faster                                      |
| 2to3                    | 161 ms                                                 | 162 ms: 1.00x slower                                       |
| scimark_fft             | 200 ms                                                 | 200 ms: 1.00x slower                                       |
| telco                   | 3.41 ms                                                | 3.42 ms: 1.00x slower                                      |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.01x slower                                       |
| sympy_integrate         | 11.5 ms                                                | 11.6 ms: 1.01x slower                                      |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.25 ms: 1.01x slower                                      |
| async_tree_io           | 704 ms                                                 | 711 ms: 1.01x slower                                       |
| sympy_expand            | 242 ms                                                 | 244 ms: 1.01x slower                                       |
| async_tree_cpu_io_mixed | 533 ms                                                 | 539 ms: 1.01x slower                                       |
| async_generators        | 196 ms                                                 | 199 ms: 1.01x slower                                       |
| pyflate                 | 310 ms                                                 | 315 ms: 1.01x slower                                       |
| regex_compile           | 76.7 ms                                                | 77.9 ms: 1.01x slower                                      |
| unpickle_list           | 2.65 us                                                | 2.70 us: 1.02x slower                                      |
| genshi_xml              | 29.8 ms                                                | 30.3 ms: 1.02x slower                                      |
| json                    | 2.78 ms                                                | 2.83 ms: 1.02x slower                                      |
| async_tree_none         | 286 ms                                                 | 291 ms: 1.02x slower                                       |
| create_gc_cycles        | 716 us                                                 | 730 us: 1.02x slower                                       |
| sqlglot_optimize        | 31.1 ms                                                | 32.0 ms: 1.03x slower                                      |
| unpickle                | 9.67 us                                                | 9.98 us: 1.03x slower                                      |
| html5lib                | 34.7 ms                                                | 36.0 ms: 1.04x slower                                      |
| richards                | 32.2 ms                                                | 33.5 ms: 1.04x slower                                      |
| float                   | 53.0 ms                                                | 55.2 ms: 1.04x slower                                      |
| async_tree_memoization  | 336 ms                                                 | 352 ms: 1.05x slower                                       |
| scimark_monte_carlo     | 46.5 ms                                                | 48.7 ms: 1.05x slower                                      |
| pprint_safe_repr        | 466 ms                                                 | 490 ms: 1.05x slower                                       |
| sqlite_synth            | 1.27 us                                                | 1.34 us: 1.05x slower                                      |
| meteor_contest          | 73.5 ms                                                | 77.4 ms: 1.05x slower                                      |
| pprint_pformat          | 954 ms                                                 | 1.01 sec: 1.06x slower                                     |
| deepcopy                | 223 us                                                 | 238 us: 1.07x slower                                       |
| deepcopy_reduce         | 1.91 us                                                | 2.06 us: 1.08x slower                                      |
| pickle_pure_python      | 201 us                                                 | 217 us: 1.08x slower                                       |
| deepcopy_memo           | 26.3 us                                                | 28.8 us: 1.09x slower                                      |
| unpickle_pure_python    | 159 us                                                 | 176 us: 1.11x slower                                       |
| comprehensions          | 16.1 us                                                | 18.3 us: 1.14x slower                                      |
| sqlglot_transpile       | 1.12 ms                                                | 1.37 ms: 1.22x slower                                      |
| sqlglot_parse           | 959 us                                                 | 1.19 ms: 1.25x slower                                      |
| mypy2                   | 195 ms                                                 | 249 ms: 1.28x slower                                       |
| Geometric mean          | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (20): tornado_http, pylint, bench_mp_pool, genshi_text, xml_etree_generate, pidigits, regex_v8, gc_traversal, scimark_sparse_mat_mult, json_dumps, chameleon, chaos, json_loads, asyncio_tcp, dulwich_log, python_startup, pathlib, pycparser, aiohttp, gunicorn
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220530-3.11.0b2-72f00f4/bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4.json: dask


# HPT report

- Reliability score: 74.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

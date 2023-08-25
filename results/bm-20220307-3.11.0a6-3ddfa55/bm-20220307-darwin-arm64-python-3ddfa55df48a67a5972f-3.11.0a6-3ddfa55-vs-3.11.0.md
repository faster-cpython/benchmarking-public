
# Results vs. 3.11.0

- fork: python
- ref: 3ddfa55df48a67a5972f
- machine: darwin-arm64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.03x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 165 ms: 1.02x slower                                                  |
| docutils       | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                |
| html5lib       | 34.7 ms                                                | 33.4 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| nbody          | 65.6 ms                                                | 66.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.08x faster                                                 |
| regex_compile  | 76.7 ms                                                | 76.2 ms: 1.01x faster                                                 |
| regex_dna      | 152 ms                                                 | 162 ms: 1.07x slower                                                  |
| regex_v8       | 16.1 ms                                                | 17.8 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| pickle_dict          | 18.0 us                                                | 17.5 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 68.3 ms: 1.03x faster                                                 |
| json_loads           | 16.1 us                                                | 16.0 us: 1.01x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.63 us: 1.01x faster                                                 |
| json_dumps           | 7.63 ms                                                | 7.65 ms: 1.00x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| unpickle             | 9.67 us                                                | 9.85 us: 1.02x slower                                                 |
| pickle_pure_python   | 201 us                                                 | 204 us: 1.02x slower                                                  |
| xml_etree_process    | 35.1 ms                                                | 36.1 ms: 1.03x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 168 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_generate, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.77 ms: 1.04x faster                                                 |
| python_startup         | 12.4 ms                                                | 15.6 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.66 ms: 1.11x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| genshi_xml      | 29.8 ms                                                | 31.2 ms: 1.05x slower                                                 |
| django_template | 21.0 ms                                                | 22.2 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| logging_simple          | 3.55 us                                                | 3.08 us: 1.15x faster                                                 |
| coverage                | 58.4 ms                                                | 50.9 ms: 1.15x faster                                                 |
| logging_format          | 3.78 us                                                | 3.36 us: 1.12x faster                                                 |
| mako                    | 8.53 ms                                                | 7.66 ms: 1.11x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.45 ms: 1.08x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| python_startup_no_site  | 10.2 ms                                                | 9.77 ms: 1.04x faster                                                 |
| html5lib                | 34.7 ms                                                | 33.4 ms: 1.04x faster                                                 |
| scimark_sor             | 82.6 ms                                                | 80.0 ms: 1.03x faster                                                 |
| pickle_dict             | 18.0 us                                                | 17.5 us: 1.03x faster                                                 |
| chaos                   | 49.4 ms                                                | 48.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse     | 70.1 ms                                                | 68.3 ms: 1.03x faster                                                 |
| pathlib                 | 27.2 ms                                                | 26.7 ms: 1.02x faster                                                 |
| hexiom                  | 4.72 ms                                                | 4.67 ms: 1.01x faster                                                 |
| genshi_text             | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| json_loads              | 16.1 us                                                | 16.0 us: 1.01x faster                                                 |
| regex_compile           | 76.7 ms                                                | 76.2 ms: 1.01x faster                                                 |
| unpickle_list           | 2.65 us                                                | 2.63 us: 1.01x faster                                                 |
| go                      | 109 ms                                                 | 108 ms: 1.01x faster                                                  |
| async_generators        | 196 ms                                                 | 195 ms: 1.01x faster                                                  |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| json_dumps              | 7.63 ms                                                | 7.65 ms: 1.00x slower                                                 |
| thrift                  | 442 us                                                 | 443 us: 1.00x slower                                                  |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.00x slower                                                 |
| async_tree_none         | 286 ms                                                 | 288 ms: 1.01x slower                                                  |
| async_tree_io           | 704 ms                                                 | 711 ms: 1.01x slower                                                  |
| json                    | 2.78 ms                                                | 2.80 ms: 1.01x slower                                                 |
| docutils                | 1.47 sec                                               | 1.49 sec: 1.01x slower                                                |
| sympy_str               | 151 ms                                                 | 153 ms: 1.01x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| fannkuch                | 261 ms                                                 | 265 ms: 1.01x slower                                                  |
| nbody                   | 65.6 ms                                                | 66.5 ms: 1.01x slower                                                 |
| generators              | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                 |
| scimark_lu              | 73.3 ms                                                | 74.4 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed | 533 ms                                                 | 542 ms: 1.02x slower                                                  |
| scimark_fft             | 200 ms                                                 | 203 ms: 1.02x slower                                                  |
| unpickle                | 9.67 us                                                | 9.85 us: 1.02x slower                                                 |
| pickle_pure_python      | 201 us                                                 | 204 us: 1.02x slower                                                  |
| create_gc_cycles        | 716 us                                                 | 729 us: 1.02x slower                                                  |
| flaskblogging           | 2.43 ms                                                | 2.48 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                 |
| nqueens                 | 59.8 ms                                                | 61.1 ms: 1.02x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.30 us: 1.02x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 75.2 ms: 1.02x slower                                                 |
| dulwich_log             | 30.3 ms                                                | 31.1 ms: 1.02x slower                                                 |
| 2to3                    | 161 ms                                                 | 165 ms: 1.02x slower                                                  |
| mdp                     | 1.55 sec                                               | 1.58 sec: 1.03x slower                                                |
| richards                | 32.2 ms                                                | 33.1 ms: 1.03x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 176 ms: 1.03x slower                                                  |
| xml_etree_process       | 35.1 ms                                                | 36.1 ms: 1.03x slower                                                 |
| raytrace                | 207 ms                                                 | 214 ms: 1.03x slower                                                  |
| pyflate                 | 310 ms                                                 | 322 ms: 1.04x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 27.4 us: 1.04x slower                                                 |
| deepcopy                | 223 us                                                 | 232 us: 1.04x slower                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 65.2 ms: 1.04x slower                                                 |
| pylint                  | 272 ms                                                 | 283 ms: 1.04x slower                                                  |
| sympy_expand            | 242 ms                                                 | 253 ms: 1.04x slower                                                  |
| telco                   | 3.41 ms                                                | 3.57 ms: 1.05x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 31.2 ms: 1.05x slower                                                 |
| pprint_pformat          | 954 ms                                                 | 999 ms: 1.05x slower                                                  |
| pprint_safe_repr        | 466 ms                                                 | 489 ms: 1.05x slower                                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.57 ms: 1.05x slower                                                 |
| coroutines              | 17.8 ms                                                | 18.7 ms: 1.05x slower                                                 |
| deepcopy_reduce         | 1.91 us                                                | 2.01 us: 1.05x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.97 ms: 1.06x slower                                                 |
| pycparser               | 698 ms                                                 | 737 ms: 1.06x slower                                                  |
| spectral_norm           | 72.6 ms                                                | 76.8 ms: 1.06x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 168 us: 1.06x slower                                                  |
| django_template         | 21.0 ms                                                | 22.2 ms: 1.06x slower                                                 |
| sqlglot_optimize        | 31.1 ms                                                | 32.9 ms: 1.06x slower                                                 |
| regex_dna               | 152 ms                                                 | 162 ms: 1.07x slower                                                  |
| bench_thread_pool       | 474 us                                                 | 513 us: 1.08x slower                                                  |
| logging_silent          | 68.1 ns                                                | 74.5 ns: 1.09x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 51.3 ms: 1.10x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 57.1 ms: 1.10x slower                                                 |
| regex_v8                | 16.1 ms                                                | 17.8 ms: 1.11x slower                                                 |
| comprehensions          | 16.1 us                                                | 18.2 us: 1.13x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.36 ms: 1.21x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.19 ms: 1.24x slower                                                 |
| python_startup          | 12.4 ms                                                | 15.6 ms: 1.25x slower                                                 |
| unpack_sequence         | 34.1 ns                                                | 90.8 ns: 2.66x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (11): sympy_sum, float, xml_etree_generate, pickle, chameleon, asyncio_tcp, aiohttp, bench_mp_pool, tornado_http, gunicorn, async_tree_memoization
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220307-3.11.0a6-3ddfa55/bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

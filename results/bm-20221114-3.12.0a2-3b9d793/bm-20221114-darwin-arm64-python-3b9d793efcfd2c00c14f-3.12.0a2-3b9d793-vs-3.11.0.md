
# Results vs. 3.11.0

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: darwin-arm64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.03x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 167 ms: 1.03x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.44 ms: 1.04x faster                                                 |
| docutils       | 1.47 sec                                               | 1.48 sec: 1.00x slower                                                |
| html5lib       | 34.7 ms                                                | 35.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| nbody          | 65.6 ms                                                | 65.8 ms: 1.00x slower                                                 |
| float          | 53.0 ms                                                | 56.3 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| regex_compile  | 76.7 ms                                                | 76.0 ms: 1.01x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.12 ms: 1.25x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 96.3 ms: 1.12x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.59 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 69.6 ms: 1.01x faster                                                 |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| xml_etree_generate   | 48.3 ms                                                | 48.7 ms: 1.01x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| xml_etree_process    | 35.1 ms                                                | 35.5 ms: 1.01x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.02x slower                                                  |
| pickle_pure_python   | 201 us                                                 | 205 us: 1.02x slower                                                  |
| unpickle             | 9.67 us                                                | 9.94 us: 1.03x slower                                                 |
| pickle               | 7.15 us                                                | 7.44 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.18 ms: 1.19x faster                                                 |
| genshi_text     | 15.3 ms                                                | 14.8 ms: 1.03x faster                                                 |
| genshi_xml      | 29.8 ms                                                | 29.6 ms: 1.01x faster                                                 |
| django_template | 21.0 ms                                                | 21.4 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 7.63 ms                                                | 6.12 ms: 1.25x faster                                                 |
| mako                    | 8.53 ms                                                | 7.18 ms: 1.19x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.79 ms: 1.14x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 96.3 ms: 1.12x faster                                                 |
| deltablue               | 2.81 ms                                                | 2.68 ms: 1.05x faster                                                 |
| scimark_lu              | 73.3 ms                                                | 70.0 ms: 1.05x faster                                                 |
| chameleon               | 4.60 ms                                                | 4.44 ms: 1.04x faster                                                 |
| genshi_text             | 15.3 ms                                                | 14.8 ms: 1.03x faster                                                 |
| create_gc_cycles        | 716 us                                                 | 693 us: 1.03x faster                                                  |
| regex_v8                | 16.1 ms                                                | 15.7 ms: 1.03x faster                                                 |
| unpickle_list           | 2.65 us                                                | 2.59 us: 1.02x faster                                                 |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| telco                   | 3.41 ms                                                | 3.35 ms: 1.02x faster                                                 |
| logging_silent          | 68.1 ns                                                | 67.1 ns: 1.01x faster                                                 |
| regex_compile           | 76.7 ms                                                | 76.0 ms: 1.01x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                 |
| genshi_xml              | 29.8 ms                                                | 29.6 ms: 1.01x faster                                                 |
| richards                | 32.2 ms                                                | 32.0 ms: 1.01x faster                                                 |
| xml_etree_iterparse     | 70.1 ms                                                | 69.6 ms: 1.01x faster                                                 |
| python_startup          | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                 |
| scimark_fft             | 200 ms                                                 | 198 ms: 1.01x faster                                                  |
| bench_thread_pool       | 474 us                                                 | 473 us: 1.00x faster                                                  |
| gc_traversal            | 2.42 ms                                                | 2.42 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| docutils                | 1.47 sec                                               | 1.48 sec: 1.00x slower                                                |
| nbody                   | 65.6 ms                                                | 65.8 ms: 1.00x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 51.9 ms: 1.00x slower                                                 |
| mdp                     | 1.55 sec                                               | 1.55 sec: 1.00x slower                                                |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| spectral_norm           | 72.6 ms                                                | 73.0 ms: 1.01x slower                                                 |
| xml_etree_generate      | 48.3 ms                                                | 48.7 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| xml_etree_process       | 35.1 ms                                                | 35.5 ms: 1.01x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 162 us: 1.02x slower                                                  |
| json                    | 2.78 ms                                                | 2.83 ms: 1.02x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.02x slower                                                 |
| django_template         | 21.0 ms                                                | 21.4 ms: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.8 ms: 1.02x slower                                                 |
| logging_simple          | 3.55 us                                                | 3.63 us: 1.02x slower                                                 |
| pickle_pure_python      | 201 us                                                 | 205 us: 1.02x slower                                                  |
| sympy_sum               | 85.5 ms                                                | 87.7 ms: 1.03x slower                                                 |
| sympy_expand            | 242 ms                                                 | 248 ms: 1.03x slower                                                  |
| unpickle                | 9.67 us                                                | 9.94 us: 1.03x slower                                                 |
| sympy_str               | 151 ms                                                 | 155 ms: 1.03x slower                                                  |
| async_tree_none         | 286 ms                                                 | 294 ms: 1.03x slower                                                  |
| chaos                   | 49.4 ms                                                | 51.0 ms: 1.03x slower                                                 |
| 2to3                    | 161 ms                                                 | 167 ms: 1.03x slower                                                  |
| html5lib                | 34.7 ms                                                | 35.9 ms: 1.03x slower                                                 |
| coverage                | 58.4 ms                                                | 60.5 ms: 1.04x slower                                                 |
| fannkuch                | 261 ms                                                 | 271 ms: 1.04x slower                                                  |
| raytrace                | 207 ms                                                 | 214 ms: 1.04x slower                                                  |
| logging_format          | 3.78 us                                                | 3.92 us: 1.04x slower                                                 |
| async_tree_cpu_io_mixed | 533 ms                                                 | 555 ms: 1.04x slower                                                  |
| pickle                  | 7.15 us                                                | 7.44 us: 1.04x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 76.7 ms: 1.04x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.17 ms: 1.04x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.01 ms: 1.05x slower                                                 |
| pprint_pformat          | 954 ms                                                 | 1.01 sec: 1.06x slower                                                |
| async_generators        | 196 ms                                                 | 208 ms: 1.06x slower                                                  |
| float                   | 53.0 ms                                                | 56.3 ms: 1.06x slower                                                 |
| pprint_safe_repr        | 466 ms                                                 | 497 ms: 1.07x slower                                                  |
| hexiom                  | 4.72 ms                                                | 5.04 ms: 1.07x slower                                                 |
| nqueens                 | 59.8 ms                                                | 63.9 ms: 1.07x slower                                                 |
| async_tree_io           | 704 ms                                                 | 755 ms: 1.07x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.07 us: 1.08x slower                                                 |
| deepcopy                | 223 us                                                 | 243 us: 1.09x slower                                                  |
| go                      | 109 ms                                                 | 119 ms: 1.10x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.40 us: 1.10x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 29.5 us: 1.12x slower                                                 |
| comprehensions          | 16.1 us                                                | 18.0 us: 1.12x slower                                                 |
| pyflate                 | 310 ms                                                 | 351 ms: 1.13x slower                                                  |
| coroutines              | 17.8 ms                                                | 20.6 ms: 1.16x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                | 54.6 ms: 1.18x slower                                                 |
| generators              | 28.8 ms                                                | 35.8 ms: 1.25x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 105 ms: 1.27x slower                                                  |
| mypy2                   | 195 ms                                                 | 264 ms: 1.36x slower                                                  |
| unpack_sequence         | 34.1 ns                                                | 62.8 ns: 1.84x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (10): pathlib, dulwich_log, tornado_http, pycparser, asyncio_tcp, python_startup_no_site, thrift, pickle_dict, async_tree_memoization, bench_mp_pool
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221114-3.12.0a2-3b9d793/bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

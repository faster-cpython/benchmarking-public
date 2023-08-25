
# Results vs. 3.11.0

- fork: python
- ref: 728e42fcf51cbb2108ca
- machine: darwin-arm64
- commit hash: 728e42f
- commit date: 2022-11-06
- overall geometric mean: 1.03x slower \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 187 ms: 1.16x slower                                                   |
| chameleon      | 4.60 ms                                                | 5.13 ms: 1.12x slower                                                  |
| docutils       | 1.47 sec                                               | 1.50 sec: 1.02x slower                                                 |
| html5lib       | 34.7 ms                                                | 37.5 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 65.9 ms: 1.00x slower                                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                   |
| float          | 53.0 ms                                                | 57.3 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                  |
| regex_compile  | 76.7 ms                                                | 77.7 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.15 ms: 1.24x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 93.3 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 65.0 ms: 1.08x faster                                                  |
| unpickle_list        | 2.65 us                                                | 2.60 us: 1.02x faster                                                  |
| unpickle             | 9.67 us                                                | 9.86 us: 1.02x slower                                                  |
| json_loads           | 16.1 us                                                | 16.4 us: 1.02x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.88 us: 1.02x slower                                                  |
| xml_etree_generate   | 48.3 ms                                                | 50.5 ms: 1.05x slower                                                  |
| unpickle_pure_python | 159 us                                                 | 167 us: 1.05x slower                                                   |
| xml_etree_process    | 35.1 ms                                                | 36.8 ms: 1.05x slower                                                  |
| pickle               | 7.15 us                                                | 7.55 us: 1.06x slower                                                  |
| pickle_pure_python   | 201 us                                                 | 222 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.38 ms: 1.38x faster                                                  |
| python_startup         | 12.4 ms                                                | 9.32 ms: 1.33x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 8.59 ms: 1.01x slower                                                  |
| django_template | 21.0 ms                                                | 22.2 ms: 1.05x slower                                                  |
| genshi_text     | 15.3 ms                                                | 16.2 ms: 1.06x slower                                                  |
| genshi_xml      | 29.8 ms                                                | 32.4 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site  | 10.2 ms                                                | 7.38 ms: 1.38x faster                                                  |
| python_startup          | 12.4 ms                                                | 9.32 ms: 1.33x faster                                                  |
| pathlib                 | 27.2 ms                                                | 20.8 ms: 1.31x faster                                                  |
| json_dumps              | 7.63 ms                                                | 6.15 ms: 1.24x faster                                                  |
| xml_etree_parse         | 108 ms                                                 | 93.3 ms: 1.16x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.76 ms: 1.16x faster                                                  |
| coverage                | 58.4 ms                                                | 53.1 ms: 1.10x faster                                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 65.0 ms: 1.08x faster                                                  |
| pylint                  | 272 ms                                                 | 257 ms: 1.06x faster                                                   |
| logging_silent          | 68.1 ns                                                | 65.6 ns: 1.04x faster                                                  |
| scimark_lu              | 73.3 ms                                                | 71.2 ms: 1.03x faster                                                  |
| bench_mp_pool           | 43.9 ms                                                | 42.8 ms: 1.03x faster                                                  |
| generators              | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                  |
| bench_thread_pool       | 474 us                                                 | 463 us: 1.02x faster                                                   |
| unpickle_list           | 2.65 us                                                | 2.60 us: 1.02x faster                                                  |
| dulwich_log             | 30.3 ms                                                | 29.7 ms: 1.02x faster                                                  |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| spectral_norm           | 72.6 ms                                                | 71.9 ms: 1.01x faster                                                  |
| nqueens                 | 59.8 ms                                                | 59.3 ms: 1.01x faster                                                  |
| richards                | 32.2 ms                                                | 32.0 ms: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                  |
| nbody                   | 65.6 ms                                                | 65.9 ms: 1.00x slower                                                  |
| mdp                     | 1.55 sec                                               | 1.55 sec: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                   |
| mako                    | 8.53 ms                                                | 8.59 ms: 1.01x slower                                                  |
| telco                   | 3.41 ms                                                | 3.44 ms: 1.01x slower                                                  |
| regex_compile           | 76.7 ms                                                | 77.7 ms: 1.01x slower                                                  |
| deltablue               | 2.81 ms                                                | 2.85 ms: 1.01x slower                                                  |
| unpickle                | 9.67 us                                                | 9.86 us: 1.02x slower                                                  |
| pycparser               | 698 ms                                                 | 711 ms: 1.02x slower                                                   |
| json_loads              | 16.1 us                                                | 16.4 us: 1.02x slower                                                  |
| docutils                | 1.47 sec                                               | 1.50 sec: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                                   |
| pickle_list             | 2.81 us                                                | 2.88 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 547 ms: 1.03x slower                                                   |
| async_generators        | 196 ms                                                 | 202 ms: 1.03x slower                                                   |
| async_tree_none         | 286 ms                                                 | 294 ms: 1.03x slower                                                   |
| sympy_sum               | 85.5 ms                                                | 88.0 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 32.0 ms: 1.03x slower                                                  |
| json                    | 2.78 ms                                                | 2.86 ms: 1.03x slower                                                  |
| fannkuch                | 261 ms                                                 | 270 ms: 1.03x slower                                                   |
| raytrace                | 207 ms                                                 | 215 ms: 1.04x slower                                                   |
| hexiom                  | 4.72 ms                                                | 4.91 ms: 1.04x slower                                                  |
| chaos                   | 49.4 ms                                                | 51.6 ms: 1.04x slower                                                  |
| async_tree_io           | 704 ms                                                 | 736 ms: 1.04x slower                                                   |
| xml_etree_generate      | 48.3 ms                                                | 50.5 ms: 1.05x slower                                                  |
| unpickle_pure_python    | 159 us                                                 | 167 us: 1.05x slower                                                   |
| xml_etree_process       | 35.1 ms                                                | 36.8 ms: 1.05x slower                                                  |
| sympy_str               | 151 ms                                                 | 159 ms: 1.05x slower                                                   |
| sympy_integrate         | 11.5 ms                                                | 12.1 ms: 1.05x slower                                                  |
| sympy_expand            | 242 ms                                                 | 255 ms: 1.05x slower                                                   |
| django_template         | 21.0 ms                                                | 22.2 ms: 1.05x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.19 ms: 1.06x slower                                                  |
| pickle                  | 7.15 us                                                | 7.55 us: 1.06x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 1.01 ms: 1.06x slower                                                  |
| genshi_text             | 15.3 ms                                                | 16.2 ms: 1.06x slower                                                  |
| logging_simple          | 3.55 us                                                | 3.77 us: 1.06x slower                                                  |
| coroutines              | 17.8 ms                                                | 19.1 ms: 1.07x slower                                                  |
| html5lib                | 34.7 ms                                                | 37.5 ms: 1.08x slower                                                  |
| float                   | 53.0 ms                                                | 57.3 ms: 1.08x slower                                                  |
| logging_format          | 3.78 us                                                | 4.09 us: 1.08x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 32.4 ms: 1.09x slower                                                  |
| meteor_contest          | 73.5 ms                                                | 80.5 ms: 1.09x slower                                                  |
| pprint_safe_repr        | 466 ms                                                 | 514 ms: 1.10x slower                                                   |
| pprint_pformat          | 954 ms                                                 | 1.05 sec: 1.10x slower                                                 |
| pickle_pure_python      | 201 us                                                 | 222 us: 1.11x slower                                                   |
| go                      | 109 ms                                                 | 121 ms: 1.11x slower                                                   |
| chameleon               | 4.60 ms                                                | 5.13 ms: 1.12x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.45 us: 1.14x slower                                                  |
| pyflate                 | 310 ms                                                 | 355 ms: 1.15x slower                                                   |
| 2to3                    | 161 ms                                                 | 187 ms: 1.16x slower                                                   |
| deepcopy                | 223 us                                                 | 263 us: 1.18x slower                                                   |
| scimark_monte_carlo     | 46.5 ms                                                | 54.9 ms: 1.18x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.28 us: 1.19x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 32.1 us: 1.22x slower                                                  |
| scimark_sor             | 82.6 ms                                                | 103 ms: 1.25x slower                                                   |
| unpack_sequence         | 34.1 ns                                                | 52.1 ns: 1.53x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (7): tornado_http, async_tree_memoization, crypto_pyaes, pickle_dict, scimark_fft, regex_v8, thrift
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, flaskblogging, gc_traversal, gunicorn, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221106-3.12.0a1+-728e42f/bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f.json: mypy


# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

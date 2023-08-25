
# Results vs. 3.11.0

- fork: python
- ref: cdde29dde90947df9bac
- machine: darwin-arm64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.03x slower \*
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 165 ms: 1.02x slower                                                   |
| chameleon      | 4.60 ms                                                | 4.42 ms: 1.04x faster                                                  |
| html5lib       | 34.7 ms                                                | 36.1 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 65.1 ms: 1.01x faster                                                  |
| float          | 53.0 ms                                                | 57.0 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_v8       | 16.1 ms                                                | 15.8 ms: 1.02x faster                                                  |
| regex_compile  | 76.7 ms                                                | 75.7 ms: 1.01x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.65 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.04 ms: 1.26x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 96.3 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 69.1 ms: 1.01x faster                                                  |
| unpickle_list        | 2.65 us                                                | 2.63 us: 1.01x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 161 us: 1.01x slower                                                   |
| xml_etree_process    | 35.1 ms                                                | 35.5 ms: 1.01x slower                                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.02x slower                                                  |
| unpickle             | 9.67 us                                                | 9.85 us: 1.02x slower                                                  |
| xml_etree_generate   | 48.3 ms                                                | 49.3 ms: 1.02x slower                                                  |
| pickle_pure_python   | 201 us                                                 | 208 us: 1.04x slower                                                   |
| pickle               | 7.15 us                                                | 7.51 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 12.4 ms                                                | 12.2 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.21 ms: 1.18x faster                                                  |
| genshi_text     | 15.3 ms                                                | 14.6 ms: 1.05x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 29.2 ms: 1.02x faster                                                  |
| django_template | 21.0 ms                                                | 21.4 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 7.63 ms                                                | 6.04 ms: 1.26x faster                                                  |
| mako                    | 8.53 ms                                                | 7.21 ms: 1.18x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.82 ms: 1.13x faster                                                  |
| xml_etree_parse         | 108 ms                                                 | 96.3 ms: 1.12x faster                                                  |
| logging_silent          | 68.1 ns                                                | 64.6 ns: 1.05x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.6 ms: 1.05x faster                                                  |
| chameleon               | 4.60 ms                                                | 4.42 ms: 1.04x faster                                                  |
| scimark_lu              | 73.3 ms                                                | 70.9 ms: 1.03x faster                                                  |
| richards                | 32.2 ms                                                | 31.2 ms: 1.03x faster                                                  |
| create_gc_cycles        | 716 us                                                 | 695 us: 1.03x faster                                                   |
| genshi_xml              | 29.8 ms                                                | 29.2 ms: 1.02x faster                                                  |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| coverage                | 58.4 ms                                                | 57.4 ms: 1.02x faster                                                  |
| python_startup          | 12.4 ms                                                | 12.2 ms: 1.02x faster                                                  |
| regex_v8                | 16.1 ms                                                | 15.8 ms: 1.02x faster                                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 69.1 ms: 1.01x faster                                                  |
| regex_compile           | 76.7 ms                                                | 75.7 ms: 1.01x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.78 ms: 1.01x faster                                                  |
| telco                   | 3.41 ms                                                | 3.37 ms: 1.01x faster                                                  |
| bench_thread_pool       | 474 us                                                 | 470 us: 1.01x faster                                                   |
| nbody                   | 65.6 ms                                                | 65.1 ms: 1.01x faster                                                  |
| unpickle_list           | 2.65 us                                                | 2.63 us: 1.01x faster                                                  |
| scimark_fft             | 200 ms                                                 | 198 ms: 1.01x faster                                                   |
| mdp                     | 1.55 sec                                               | 1.54 sec: 1.00x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.65 ms: 1.01x slower                                                  |
| spectral_norm           | 72.6 ms                                                | 73.2 ms: 1.01x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.4 ms: 1.01x slower                                                  |
| async_tree_none         | 286 ms                                                 | 289 ms: 1.01x slower                                                   |
| sqlglot_normalize       | 171 ms                                                 | 173 ms: 1.01x slower                                                   |
| unpickle_pure_python    | 159 us                                                 | 161 us: 1.01x slower                                                   |
| xml_etree_process       | 35.1 ms                                                | 35.5 ms: 1.01x slower                                                  |
| json                    | 2.78 ms                                                | 2.82 ms: 1.01x slower                                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.02x slower                                                  |
| logging_simple          | 3.55 us                                                | 3.60 us: 1.02x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.02x slower                                                  |
| django_template         | 21.0 ms                                                | 21.4 ms: 1.02x slower                                                  |
| sympy_sum               | 85.5 ms                                                | 87.0 ms: 1.02x slower                                                  |
| unpickle                | 9.67 us                                                | 9.85 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 544 ms: 1.02x slower                                                   |
| raytrace                | 207 ms                                                 | 211 ms: 1.02x slower                                                   |
| sympy_str               | 151 ms                                                 | 154 ms: 1.02x slower                                                   |
| xml_etree_generate      | 48.3 ms                                                | 49.3 ms: 1.02x slower                                                  |
| 2to3                    | 161 ms                                                 | 165 ms: 1.02x slower                                                   |
| sympy_expand            | 242 ms                                                 | 247 ms: 1.02x slower                                                   |
| chaos                   | 49.4 ms                                                | 50.7 ms: 1.03x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.1 ms: 1.03x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.16 ms: 1.03x slower                                                  |
| nqueens                 | 59.8 ms                                                | 61.8 ms: 1.03x slower                                                  |
| logging_format          | 3.78 us                                                | 3.91 us: 1.03x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 994 us: 1.04x slower                                                   |
| fannkuch                | 261 ms                                                 | 271 ms: 1.04x slower                                                   |
| pickle_pure_python      | 201 us                                                 | 208 us: 1.04x slower                                                   |
| html5lib                | 34.7 ms                                                | 36.1 ms: 1.04x slower                                                  |
| hexiom                  | 4.72 ms                                                | 4.93 ms: 1.04x slower                                                  |
| async_generators        | 196 ms                                                 | 205 ms: 1.04x slower                                                   |
| meteor_contest          | 73.5 ms                                                | 77.2 ms: 1.05x slower                                                  |
| pickle                  | 7.15 us                                                | 7.51 us: 1.05x slower                                                  |
| async_tree_io           | 704 ms                                                 | 745 ms: 1.06x slower                                                   |
| pprint_pformat          | 954 ms                                                 | 1.01 sec: 1.06x slower                                                 |
| pprint_safe_repr        | 466 ms                                                 | 497 ms: 1.07x slower                                                   |
| float                   | 53.0 ms                                                | 57.0 ms: 1.08x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.07 us: 1.08x slower                                                  |
| go                      | 109 ms                                                 | 118 ms: 1.09x slower                                                   |
| deepcopy                | 223 us                                                 | 244 us: 1.09x slower                                                   |
| sqlite_synth            | 1.27 us                                                | 1.39 us: 1.10x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 29.0 us: 1.10x slower                                                  |
| comprehensions          | 16.1 us                                                | 17.8 us: 1.10x slower                                                  |
| coroutines              | 17.8 ms                                                | 19.9 ms: 1.12x slower                                                  |
| pyflate                 | 310 ms                                                 | 350 ms: 1.13x slower                                                   |
| scimark_monte_carlo     | 46.5 ms                                                | 54.7 ms: 1.18x slower                                                  |
| generators              | 28.8 ms                                                | 34.3 ms: 1.19x slower                                                  |
| scimark_sor             | 82.6 ms                                                | 104 ms: 1.25x slower                                                   |
| mypy2                   | 195 ms                                                 | 263 ms: 1.35x slower                                                   |
| unpack_sequence         | 34.1 ns                                                | 62.4 ns: 1.83x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (14): tornado_http, async_tree_memoization, pathlib, pycparser, dulwich_log, pickle_list, pickle_dict, python_startup_no_site, thrift, gc_traversal, docutils, pidigits, asyncio_tcp, bench_mp_pool
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221121-3.12.0a2+-cdde29d/bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d.json: dask


# HPT report

- Reliability score: 99.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c4e4b91
- commit date: 2022-02-03
- overall geometric mean: 1.04x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 267 ms: 1.03x slower                                  |
| chameleon      | 6.47 ms                                                | 6.95 ms: 1.07x slower                                 |
| html5lib       | 64.5 ms                                                | 67.9 ms: 1.05x slower                                 |
| tornado_http   | 96.3 ms                                                | 106 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                  |
| nbody          | 93.1 ms                                                | 94.7 ms: 1.02x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.14 ms: 1.27x faster                                 |
| regex_compile  | 138 ms                                                 | 140 ms: 1.02x slower                                  |
| regex_dna      | 204 ms                                                 | 213 ms: 1.04x slower                                  |
| regex_v8       | 22.0 ms                                                | 24.0 ms: 1.09x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 28.1 us: 1.11x faster                                 |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                  |
| json_dumps           | 12.6 ms                                                | 12.2 ms: 1.03x faster                                 |
| pickle               | 10.1 us                                                | 9.93 us: 1.01x faster                                 |
| json_loads           | 26.5 us                                                | 26.7 us: 1.01x slower                                 |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 79.6 ms: 1.04x slower                                 |
| xml_etree_process    | 53.9 ms                                                | 57.0 ms: 1.06x slower                                 |
| unpickle_list        | 4.91 us                                                | 5.26 us: 1.07x slower                                 |
| pickle_list          | 4.11 us                                                | 4.47 us: 1.09x slower                                 |
| pickle_pure_python   | 306 us                                                 | 334 us: 1.09x slower                                  |
| unpickle_pure_python | 228 us                                                 | 249 us: 1.09x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.13 ms: 1.05x faster                                 |
| python_startup_no_site | 6.01 ms                                                | 5.92 ms: 1.02x faster                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 10.1 ms                                                | 10.5 ms: 1.04x slower                                 |
| django_template | 32.6 ms                                                | 35.4 ms: 1.09x slower                                 |
| Geometric mean  | (ref)                                                  | 1.06x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.14 ms: 1.27x faster                                 |
| pickle_dict             | 31.1 us                                                | 28.1 us: 1.11x faster                                 |
| logging_format          | 6.68 us                                                | 6.37 us: 1.05x faster                                 |
| python_startup          | 8.52 ms                                                | 8.13 ms: 1.05x faster                                 |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 153 ms: 1.04x faster                                  |
| logging_simple          | 6.03 us                                                | 5.84 us: 1.03x faster                                 |
| json_dumps              | 12.6 ms                                                | 12.2 ms: 1.03x faster                                 |
| json                    | 4.94 ms                                                | 4.84 ms: 1.02x faster                                 |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                  |
| python_startup_no_site  | 6.01 ms                                                | 5.92 ms: 1.02x faster                                 |
| pickle                  | 10.1 us                                                | 9.93 us: 1.01x faster                                 |
| json_loads              | 26.5 us                                                | 26.7 us: 1.01x slower                                 |
| pycparser               | 1.18 sec                                               | 1.19 sec: 1.01x slower                                |
| pathlib                 | 18.2 ms                                                | 18.5 ms: 1.01x slower                                 |
| sympy_integrate         | 21.0 ms                                                | 21.3 ms: 1.01x slower                                 |
| regex_compile           | 138 ms                                                 | 140 ms: 1.02x slower                                  |
| nbody                   | 93.1 ms                                                | 94.7 ms: 1.02x slower                                 |
| telco                   | 6.58 ms                                                | 6.70 ms: 1.02x slower                                 |
| sympy_sum               | 167 ms                                                 | 170 ms: 1.02x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                  |
| 2to3                    | 259 ms                                                 | 267 ms: 1.03x slower                                  |
| dulwich_log             | 63.7 ms                                                | 65.7 ms: 1.03x slower                                 |
| fannkuch                | 388 ms                                                 | 400 ms: 1.03x slower                                  |
| mako                    | 10.1 ms                                                | 10.5 ms: 1.04x slower                                 |
| regex_dna               | 204 ms                                                 | 213 ms: 1.04x slower                                  |
| spectral_norm           | 100 ms                                                 | 104 ms: 1.04x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 79.6 ms: 1.04x slower                                 |
| nqueens                 | 83.4 ms                                                | 87.2 ms: 1.05x slower                                 |
| sympy_str               | 290 ms                                                 | 304 ms: 1.05x slower                                  |
| html5lib                | 64.5 ms                                                | 67.9 ms: 1.05x slower                                 |
| go                      | 140 ms                                                 | 147 ms: 1.05x slower                                  |
| scimark_fft             | 328 ms                                                 | 347 ms: 1.06x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 57.0 ms: 1.06x slower                                 |
| sympy_expand            | 475 ms                                                 | 503 ms: 1.06x slower                                  |
| hexiom                  | 6.37 ms                                                | 6.76 ms: 1.06x slower                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 72.6 ms: 1.07x slower                                 |
| unpack_sequence         | 43.1 ns                                                | 46.0 ns: 1.07x slower                                 |
| unpickle_list           | 4.91 us                                                | 5.26 us: 1.07x slower                                 |
| chameleon               | 6.47 ms                                                | 6.95 ms: 1.07x slower                                 |
| sqlite_synth            | 2.52 us                                                | 2.71 us: 1.07x slower                                 |
| thrift                  | 756 us                                                 | 815 us: 1.08x slower                                  |
| raytrace                | 297 ms                                                 | 321 ms: 1.08x slower                                  |
| chaos                   | 69.2 ms                                                | 74.9 ms: 1.08x slower                                 |
| django_template         | 32.6 ms                                                | 35.4 ms: 1.09x slower                                 |
| pickle_list             | 4.11 us                                                | 4.47 us: 1.09x slower                                 |
| regex_v8                | 22.0 ms                                                | 24.0 ms: 1.09x slower                                 |
| scimark_sor             | 118 ms                                                 | 129 ms: 1.09x slower                                  |
| pickle_pure_python      | 306 us                                                 | 334 us: 1.09x slower                                  |
| unpickle_pure_python    | 228 us                                                 | 249 us: 1.09x slower                                  |
| scimark_lu              | 110 ms                                                 | 120 ms: 1.09x slower                                  |
| tornado_http            | 96.3 ms                                                | 106 ms: 1.10x slower                                  |
| pyflate                 | 418 ms                                                 | 459 ms: 1.10x slower                                  |
| richards                | 45.7 ms                                                | 50.8 ms: 1.11x slower                                 |
| logging_silent          | 101 ns                                                 | 113 ns: 1.12x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 83.8 ms: 1.12x slower                                 |
| deltablue               | 3.67 ms                                                | 4.13 ms: 1.13x slower                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 5.14 ms: 1.14x slower                                 |
| Geometric mean          | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (2): unpickle, float
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

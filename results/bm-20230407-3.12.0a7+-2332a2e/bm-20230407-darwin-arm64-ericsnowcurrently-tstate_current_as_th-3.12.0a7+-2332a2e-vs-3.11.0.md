
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: darwin-arm64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.03x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 173 ms: 1.07x slower                                                              |
| chameleon      | 4.60 ms                                                | 4.69 ms: 1.02x slower                                                             |
| docutils       | 1.47 sec                                               | 1.54 sec: 1.05x slower                                                            |
| html5lib       | 34.7 ms                                                | 37.7 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 280 ms: 1.00x faster                                                              |
| float          | 53.0 ms                                                | 56.2 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.65 ms: 1.01x slower                                                             |
| regex_v8       | 16.1 ms                                                | 16.2 ms: 1.01x slower                                                             |
| regex_compile  | 76.7 ms                                                | 78.5 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.39 ms: 1.19x faster                                                             |
| unpickle_pure_python | 159 us                                                 | 148 us: 1.08x faster                                                              |
| unpickle             | 9.67 us                                                | 9.27 us: 1.04x faster                                                             |
| pickle_pure_python   | 201 us                                                 | 192 us: 1.04x faster                                                              |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                              |
| json_loads           | 16.1 us                                                | 16.4 us: 1.02x slower                                                             |
| pickle_dict          | 18.0 us                                                | 18.7 us: 1.04x slower                                                             |
| xml_etree_iterparse  | 70.1 ms                                                | 73.4 ms: 1.05x slower                                                             |
| pickle               | 7.15 us                                                | 7.65 us: 1.07x slower                                                             |
| unpickle_list        | 2.65 us                                                | 2.90 us: 1.09x slower                                                             |
| xml_etree_process    | 35.1 ms                                                | 38.5 ms: 1.10x slower                                                             |
| pickle_list          | 2.81 us                                                | 3.12 us: 1.11x slower                                                             |
| xml_etree_generate   | 48.3 ms                                                | 56.2 ms: 1.16x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 11.9 ms: 1.04x faster                                                             |
| python_startup_no_site | 10.2 ms                                                | 9.92 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.34 ms: 1.16x faster                                                             |
| genshi_text     | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                             |
| genshi_xml      | 29.8 ms                                                | 30.3 ms: 1.02x slower                                                             |
| django_template | 21.0 ms                                                | 22.6 ms: 1.08x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 448 ms: 1.45x faster                                                              |
| json_dumps              | 7.63 ms                                                | 6.39 ms: 1.19x faster                                                             |
| mako                    | 8.53 ms                                                | 7.34 ms: 1.16x faster                                                             |
| generators              | 28.8 ms                                                | 26.2 ms: 1.10x faster                                                             |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.95 ms: 1.08x faster                                                             |
| unpickle_pure_python    | 159 us                                                 | 148 us: 1.08x faster                                                              |
| deltablue               | 2.81 ms                                                | 2.62 ms: 1.07x faster                                                             |
| sqlglot_parse           | 959 us                                                 | 905 us: 1.06x faster                                                              |
| hexiom                  | 4.72 ms                                                | 4.47 ms: 1.06x faster                                                             |
| richards                | 32.2 ms                                                | 30.8 ms: 1.05x faster                                                             |
| python_startup          | 12.4 ms                                                | 11.9 ms: 1.04x faster                                                             |
| unpickle                | 9.67 us                                                | 9.27 us: 1.04x faster                                                             |
| pickle_pure_python      | 201 us                                                 | 192 us: 1.04x faster                                                              |
| sqlglot_transpile       | 1.12 ms                                                | 1.08 ms: 1.04x faster                                                             |
| genshi_text             | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                             |
| xml_etree_parse         | 108 ms                                                 | 105 ms: 1.03x faster                                                              |
| scimark_fft             | 200 ms                                                 | 194 ms: 1.03x faster                                                              |
| python_startup_no_site  | 10.2 ms                                                | 9.92 ms: 1.02x faster                                                             |
| deepcopy_memo           | 26.3 us                                                | 25.8 us: 1.02x faster                                                             |
| create_gc_cycles        | 716 us                                                 | 707 us: 1.01x faster                                                              |
| unpack_sequence         | 34.1 ns                                                | 33.8 ns: 1.01x faster                                                             |
| logging_silent          | 68.1 ns                                                | 67.8 ns: 1.00x faster                                                             |
| chaos                   | 49.4 ms                                                | 49.3 ms: 1.00x faster                                                             |
| pidigits                | 281 ms                                                 | 280 ms: 1.00x faster                                                              |
| coverage                | 58.4 ms                                                | 58.8 ms: 1.01x slower                                                             |
| meteor_contest          | 73.5 ms                                                | 74.0 ms: 1.01x slower                                                             |
| regex_effbot            | 2.63 ms                                                | 2.65 ms: 1.01x slower                                                             |
| regex_v8                | 16.1 ms                                                | 16.2 ms: 1.01x slower                                                             |
| spectral_norm           | 72.6 ms                                                | 73.3 ms: 1.01x slower                                                             |
| mdp                     | 1.55 sec                                               | 1.56 sec: 1.01x slower                                                            |
| genshi_xml              | 29.8 ms                                                | 30.3 ms: 1.02x slower                                                             |
| dulwich_log             | 30.3 ms                                                | 30.9 ms: 1.02x slower                                                             |
| json                    | 2.78 ms                                                | 2.83 ms: 1.02x slower                                                             |
| chameleon               | 4.60 ms                                                | 4.69 ms: 1.02x slower                                                             |
| json_loads              | 16.1 us                                                | 16.4 us: 1.02x slower                                                             |
| regex_compile           | 76.7 ms                                                | 78.5 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed | 533 ms                                                 | 548 ms: 1.03x slower                                                              |
| pathlib                 | 27.2 ms                                                | 28.1 ms: 1.03x slower                                                             |
| async_tree_none         | 286 ms                                                 | 295 ms: 1.03x slower                                                              |
| deepcopy                | 223 us                                                 | 231 us: 1.04x slower                                                              |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.48 ms: 1.04x slower                                                             |
| pickle_dict             | 18.0 us                                                | 18.7 us: 1.04x slower                                                             |
| comprehensions          | 16.1 us                                                | 16.8 us: 1.04x slower                                                             |
| xml_etree_iterparse     | 70.1 ms                                                | 73.4 ms: 1.05x slower                                                             |
| bench_thread_pool       | 474 us                                                 | 497 us: 1.05x slower                                                              |
| docutils                | 1.47 sec                                               | 1.54 sec: 1.05x slower                                                            |
| sympy_integrate         | 11.5 ms                                                | 12.2 ms: 1.06x slower                                                             |
| pprint_pformat          | 954 ms                                                 | 1.01 sec: 1.06x slower                                                            |
| crypto_pyaes            | 51.7 ms                                                | 54.7 ms: 1.06x slower                                                             |
| float                   | 53.0 ms                                                | 56.2 ms: 1.06x slower                                                             |
| go                      | 109 ms                                                 | 115 ms: 1.06x slower                                                              |
| bench_mp_pool           | 43.9 ms                                                | 46.8 ms: 1.07x slower                                                             |
| pprint_safe_repr        | 466 ms                                                 | 497 ms: 1.07x slower                                                              |
| async_tree_io           | 704 ms                                                 | 752 ms: 1.07x slower                                                              |
| logging_simple          | 3.55 us                                                | 3.79 us: 1.07x slower                                                             |
| pickle                  | 7.15 us                                                | 7.65 us: 1.07x slower                                                             |
| gc_traversal            | 2.42 ms                                                | 2.59 ms: 1.07x slower                                                             |
| 2to3                    | 161 ms                                                 | 173 ms: 1.07x slower                                                              |
| coroutines              | 17.8 ms                                                | 19.1 ms: 1.07x slower                                                             |
| deepcopy_reduce         | 1.91 us                                                | 2.05 us: 1.07x slower                                                             |
| django_template         | 21.0 ms                                                | 22.6 ms: 1.08x slower                                                             |
| sqlalchemy_declarative  | 62.6 ms                                                | 67.5 ms: 1.08x slower                                                             |
| telco                   | 3.41 ms                                                | 3.68 ms: 1.08x slower                                                             |
| sqlglot_optimize        | 31.1 ms                                                | 33.7 ms: 1.08x slower                                                             |
| sqlglot_normalize       | 171 ms                                                 | 185 ms: 1.09x slower                                                              |
| html5lib                | 34.7 ms                                                | 37.7 ms: 1.09x slower                                                             |
| fannkuch                | 261 ms                                                 | 284 ms: 1.09x slower                                                              |
| logging_format          | 3.78 us                                                | 4.11 us: 1.09x slower                                                             |
| scimark_sor             | 82.6 ms                                                | 90.0 ms: 1.09x slower                                                             |
| unpickle_list           | 2.65 us                                                | 2.90 us: 1.09x slower                                                             |
| sympy_sum               | 85.5 ms                                                | 93.6 ms: 1.09x slower                                                             |
| sympy_str               | 151 ms                                                 | 166 ms: 1.10x slower                                                              |
| xml_etree_process       | 35.1 ms                                                | 38.5 ms: 1.10x slower                                                             |
| pyflate                 | 310 ms                                                 | 341 ms: 1.10x slower                                                              |
| nqueens                 | 59.8 ms                                                | 65.7 ms: 1.10x slower                                                             |
| sympy_expand            | 242 ms                                                 | 267 ms: 1.10x slower                                                              |
| pickle_list             | 2.81 us                                                | 3.12 us: 1.11x slower                                                             |
| scimark_monte_carlo     | 46.5 ms                                                | 52.2 ms: 1.12x slower                                                             |
| thrift                  | 442 us                                                 | 501 us: 1.13x slower                                                              |
| raytrace                | 207 ms                                                 | 240 ms: 1.16x slower                                                              |
| xml_etree_generate      | 48.3 ms                                                | 56.2 ms: 1.16x slower                                                             |
| sqlite_synth            | 1.27 us                                                | 1.54 us: 1.21x slower                                                             |
| mypy2                   | 195 ms                                                 | 271 ms: 1.39x slower                                                              |
| async_generators        | 196 ms                                                 | 301 ms: 1.53x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.03x slower                                                                      |

Benchmark hidden because not significant (6): tornado_http, pycparser, scimark_lu, regex_dna, nbody, async_tree_memoization
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230407-3.12.0a7+-2332a2e/bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x


# Results vs. base

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: darwin-arm64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                                 | 173 ms: 1.03x slower                                                              |
| chameleon      | 4.49 ms                                                                | 4.69 ms: 1.05x slower                                                             |
| docutils       | 1.50 sec                                                               | 1.54 sec: 1.03x slower                                                            |
| html5lib       | 36.6 ms                                                                | 37.7 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 53.0 ms                                                                | 56.2 ms: 1.06x slower                                                             |
| nbody          | 60.4 ms                                                                | 65.6 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 2.66 ms                                                                | 2.65 ms: 1.01x faster                                                             |
| regex_v8       | 16.0 ms                                                                | 16.2 ms: 1.01x slower                                                             |
| regex_compile  | 76.6 ms                                                                | 78.5 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 148 us                                                                 | 148 us: 1.00x faster                                                              |
| pickle               | 7.59 us                                                                | 7.65 us: 1.01x slower                                                             |
| xml_etree_iterparse  | 71.9 ms                                                                | 73.4 ms: 1.02x slower                                                             |
| unpickle             | 9.07 us                                                                | 9.27 us: 1.02x slower                                                             |
| pickle_dict          | 18.3 us                                                                | 18.7 us: 1.02x slower                                                             |
| xml_etree_parse      | 102 ms                                                                 | 105 ms: 1.03x slower                                                              |
| json_dumps           | 6.22 ms                                                                | 6.39 ms: 1.03x slower                                                             |
| xml_etree_process    | 36.8 ms                                                                | 38.5 ms: 1.05x slower                                                             |
| pickle_list          | 2.94 us                                                                | 3.12 us: 1.06x slower                                                             |
| xml_etree_generate   | 51.4 ms                                                                | 56.2 ms: 1.09x slower                                                             |
| unpickle_list        | 2.64 us                                                                | 2.90 us: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                                      |

Benchmark hidden because not significant (2): pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 10.0 ms                                                                | 9.92 ms: 1.01x faster                                                             |
| python_startup         | 12.0 ms                                                                | 11.9 ms: 1.01x faster                                                             |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 7.39 ms                                                                | 7.34 ms: 1.01x faster                                                             |
| genshi_text     | 14.7 ms                                                                | 14.7 ms: 1.00x slower                                                             |
| genshi_xml      | 29.3 ms                                                                | 30.3 ms: 1.03x slower                                                             |
| django_template | 21.7 ms                                                                | 22.6 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 27.6 ms                                                                | 26.2 ms: 1.05x faster                                                             |
| coverage                | 61.1 ms                                                                | 58.8 ms: 1.04x faster                                                             |
| richards                | 31.5 ms                                                                | 30.8 ms: 1.02x faster                                                             |
| python_startup_no_site  | 10.0 ms                                                                | 9.92 ms: 1.01x faster                                                             |
| go                      | 116 ms                                                                 | 115 ms: 1.01x faster                                                              |
| mako                    | 7.39 ms                                                                | 7.34 ms: 1.01x faster                                                             |
| regex_effbot            | 2.66 ms                                                                | 2.65 ms: 1.01x faster                                                             |
| python_startup          | 12.0 ms                                                                | 11.9 ms: 1.01x faster                                                             |
| pyflate                 | 343 ms                                                                 | 341 ms: 1.01x faster                                                              |
| deepcopy_memo           | 25.9 us                                                                | 25.8 us: 1.00x faster                                                             |
| scimark_monte_carlo     | 52.4 ms                                                                | 52.2 ms: 1.00x faster                                                             |
| unpickle_pure_python    | 148 us                                                                 | 148 us: 1.00x faster                                                              |
| spectral_norm           | 73.1 ms                                                                | 73.3 ms: 1.00x slower                                                             |
| sqlglot_parse           | 902 us                                                                 | 905 us: 1.00x slower                                                              |
| deltablue               | 2.61 ms                                                                | 2.62 ms: 1.00x slower                                                             |
| genshi_text             | 14.7 ms                                                                | 14.7 ms: 1.00x slower                                                             |
| sqlglot_transpile       | 1.07 ms                                                                | 1.08 ms: 1.00x slower                                                             |
| async_tree_cpu_io_mixed | 545 ms                                                                 | 548 ms: 1.01x slower                                                              |
| pickle                  | 7.59 us                                                                | 7.65 us: 1.01x slower                                                             |
| create_gc_cycles        | 701 us                                                                 | 707 us: 1.01x slower                                                              |
| regex_v8                | 16.0 ms                                                                | 16.2 ms: 1.01x slower                                                             |
| logging_silent          | 67.0 ns                                                                | 67.8 ns: 1.01x slower                                                             |
| hexiom                  | 4.42 ms                                                                | 4.47 ms: 1.01x slower                                                             |
| coroutines              | 18.8 ms                                                                | 19.1 ms: 1.01x slower                                                             |
| json                    | 2.79 ms                                                                | 2.83 ms: 1.01x slower                                                             |
| unpack_sequence         | 33.2 ns                                                                | 33.8 ns: 1.02x slower                                                             |
| logging_format          | 4.04 us                                                                | 4.11 us: 1.02x slower                                                             |
| bench_mp_pool           | 46.0 ms                                                                | 46.8 ms: 1.02x slower                                                             |
| mdp                     | 1.53 sec                                                               | 1.56 sec: 1.02x slower                                                            |
| dask                    | 324 ms                                                                 | 330 ms: 1.02x slower                                                              |
| pycparser               | 681 ms                                                                 | 695 ms: 1.02x slower                                                              |
| meteor_contest          | 72.5 ms                                                                | 74.0 ms: 1.02x slower                                                             |
| async_tree_io           | 736 ms                                                                 | 752 ms: 1.02x slower                                                              |
| scimark_sor             | 88.2 ms                                                                | 90.0 ms: 1.02x slower                                                             |
| xml_etree_iterparse     | 71.9 ms                                                                | 73.4 ms: 1.02x slower                                                             |
| pathlib                 | 27.5 ms                                                                | 28.1 ms: 1.02x slower                                                             |
| unpickle                | 9.07 us                                                                | 9.27 us: 1.02x slower                                                             |
| pickle_dict             | 18.3 us                                                                | 18.7 us: 1.02x slower                                                             |
| async_tree_none         | 288 ms                                                                 | 295 ms: 1.02x slower                                                              |
| regex_compile           | 76.6 ms                                                                | 78.5 ms: 1.02x slower                                                             |
| scimark_lu              | 71.5 ms                                                                | 73.3 ms: 1.02x slower                                                             |
| xml_etree_parse         | 102 ms                                                                 | 105 ms: 1.03x slower                                                              |
| comprehensions          | 16.4 us                                                                | 16.8 us: 1.03x slower                                                             |
| json_dumps              | 6.22 ms                                                                | 6.39 ms: 1.03x slower                                                             |
| logging_simple          | 3.69 us                                                                | 3.79 us: 1.03x slower                                                             |
| html5lib                | 36.6 ms                                                                | 37.7 ms: 1.03x slower                                                             |
| dulwich_log             | 30.0 ms                                                                | 30.9 ms: 1.03x slower                                                             |
| 2to3                    | 168 ms                                                                 | 173 ms: 1.03x slower                                                              |
| docutils                | 1.50 sec                                                               | 1.54 sec: 1.03x slower                                                            |
| scimark_fft             | 188 ms                                                                 | 194 ms: 1.03x slower                                                              |
| sympy_integrate         | 11.8 ms                                                                | 12.2 ms: 1.03x slower                                                             |
| genshi_xml              | 29.3 ms                                                                | 30.3 ms: 1.03x slower                                                             |
| sqlalchemy_imperative   | 7.21 ms                                                                | 7.48 ms: 1.04x slower                                                             |
| scimark_sparse_mat_mult | 2.84 ms                                                                | 2.95 ms: 1.04x slower                                                             |
| nqueens                 | 63.3 ms                                                                | 65.7 ms: 1.04x slower                                                             |
| pprint_pformat          | 969 ms                                                                 | 1.01 sec: 1.04x slower                                                            |
| deepcopy                | 221 us                                                                 | 231 us: 1.04x slower                                                              |
| django_template         | 21.7 ms                                                                | 22.6 ms: 1.04x slower                                                             |
| chaos                   | 47.3 ms                                                                | 49.3 ms: 1.04x slower                                                             |
| xml_etree_process       | 36.8 ms                                                                | 38.5 ms: 1.05x slower                                                             |
| chameleon               | 4.49 ms                                                                | 4.69 ms: 1.05x slower                                                             |
| sqlalchemy_declarative  | 64.6 ms                                                                | 67.5 ms: 1.05x slower                                                             |
| pprint_safe_repr        | 475 ms                                                                 | 497 ms: 1.05x slower                                                              |
| bench_thread_pool       | 472 us                                                                 | 497 us: 1.05x slower                                                              |
| sympy_sum               | 88.9 ms                                                                | 93.6 ms: 1.05x slower                                                             |
| sqlglot_optimize        | 32.0 ms                                                                | 33.7 ms: 1.05x slower                                                             |
| deepcopy_reduce         | 1.95 us                                                                | 2.05 us: 1.05x slower                                                             |
| sqlglot_normalize       | 176 ms                                                                 | 185 ms: 1.06x slower                                                              |
| fannkuch                | 268 ms                                                                 | 284 ms: 1.06x slower                                                              |
| pickle_list             | 2.94 us                                                                | 3.12 us: 1.06x slower                                                             |
| float                   | 53.0 ms                                                                | 56.2 ms: 1.06x slower                                                             |
| sympy_str               | 156 ms                                                                 | 166 ms: 1.06x slower                                                              |
| telco                   | 3.46 ms                                                                | 3.68 ms: 1.06x slower                                                             |
| gc_traversal            | 2.43 ms                                                                | 2.59 ms: 1.07x slower                                                             |
| sympy_expand            | 248 ms                                                                 | 267 ms: 1.08x slower                                                              |
| raytrace                | 222 ms                                                                 | 240 ms: 1.09x slower                                                              |
| nbody                   | 60.4 ms                                                                | 65.6 ms: 1.09x slower                                                             |
| xml_etree_generate      | 51.4 ms                                                                | 56.2 ms: 1.09x slower                                                             |
| thrift                  | 458 us                                                                 | 501 us: 1.09x slower                                                              |
| unpickle_list           | 2.64 us                                                                | 2.90 us: 1.10x slower                                                             |
| sqlite_synth            | 1.36 us                                                                | 1.54 us: 1.13x slower                                                             |
| async_generators        | 263 ms                                                                 | 301 ms: 1.14x slower                                                              |
| Geometric mean          | (ref)                                                                  | 1.03x slower                                                                      |

Benchmark hidden because not significant (9): asyncio_tcp, pickle_pure_python, regex_dna, crypto_pyaes, pidigits, json_loads, async_tree_memoization, mypy2, tornado_http

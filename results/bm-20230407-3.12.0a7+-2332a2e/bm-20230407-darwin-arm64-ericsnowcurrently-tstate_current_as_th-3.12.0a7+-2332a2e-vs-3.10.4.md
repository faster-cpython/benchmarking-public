
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: darwin-arm64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.17x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 173 ms: 1.17x faster                                                              |
| chameleon      | 5.84 ms                                                | 4.69 ms: 1.25x faster                                                             |
| docutils       | 1.78 sec                                               | 1.54 sec: 1.15x faster                                                            |
| html5lib       | 44.1 ms                                                | 37.7 ms: 1.17x faster                                                             |
| tornado_http   | 91.9 ms                                                | 70.8 ms: 1.30x faster                                                             |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 65.6 ms: 1.43x faster                                                             |
| float          | 72.3 ms                                                | 56.2 ms: 1.29x faster                                                             |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 78.5 ms: 1.23x faster                                                             |
| regex_v8       | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                             |
| regex_dna      | 160 ms                                                 | 152 ms: 1.05x faster                                                              |
| regex_effbot   | 2.45 ms                                                | 2.65 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 192 us: 1.47x faster                                                              |
| unpickle_pure_python | 203 us                                                 | 148 us: 1.38x faster                                                              |
| json_dumps           | 8.38 ms                                                | 6.39 ms: 1.31x faster                                                             |
| xml_etree_process    | 45.1 ms                                                | 38.5 ms: 1.17x faster                                                             |
| unpickle             | 9.77 us                                                | 9.27 us: 1.05x faster                                                             |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                                             |
| xml_etree_parse      | 107 ms                                                 | 105 ms: 1.02x faster                                                              |
| xml_etree_iterparse  | 72.6 ms                                                | 73.4 ms: 1.01x slower                                                             |
| xml_etree_generate   | 54.3 ms                                                | 56.2 ms: 1.04x slower                                                             |
| pickle               | 7.36 us                                                | 7.65 us: 1.04x slower                                                             |
| pickle_dict          | 17.8 us                                                | 18.7 us: 1.05x slower                                                             |
| unpickle_list        | 2.66 us                                                | 2.90 us: 1.09x slower                                                             |
| pickle_list          | 2.83 us                                                | 3.12 us: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.9 ms: 1.06x faster                                                             |
| python_startup_no_site | 9.73 ms                                                | 9.92 ms: 1.02x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.34 ms: 1.43x faster                                                             |
| genshi_text     | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                             |
| genshi_xml      | 37.6 ms                                                | 30.3 ms: 1.24x faster                                                             |
| django_template | 27.3 ms                                                | 22.6 ms: 1.21x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.62 ms: 1.97x faster                                                             |
| logging_silent          | 119 ns                                                 | 67.8 ns: 1.76x faster                                                             |
| richards                | 51.4 ms                                                | 30.8 ms: 1.67x faster                                                             |
| asyncio_tcp             | 673 ms                                                 | 448 ms: 1.50x faster                                                              |
| scimark_lu              | 110 ms                                                 | 73.3 ms: 1.50x faster                                                             |
| pickle_pure_python      | 284 us                                                 | 192 us: 1.47x faster                                                              |
| sqlglot_parse           | 1.33 ms                                                | 905 us: 1.47x faster                                                              |
| async_tree_memoization  | 493 ms                                                 | 343 ms: 1.44x faster                                                              |
| nbody                   | 94.1 ms                                                | 65.6 ms: 1.43x faster                                                             |
| go                      | 165 ms                                                 | 115 ms: 1.43x faster                                                              |
| mako                    | 10.5 ms                                                | 7.34 ms: 1.43x faster                                                             |
| sqlglot_transpile       | 1.54 ms                                                | 1.08 ms: 1.43x faster                                                             |
| crypto_pyaes            | 78.0 ms                                                | 54.7 ms: 1.43x faster                                                             |
| hexiom                  | 6.32 ms                                                | 4.47 ms: 1.41x faster                                                             |
| scimark_sor             | 127 ms                                                 | 90.0 ms: 1.41x faster                                                             |
| scimark_monte_carlo     | 72.2 ms                                                | 52.2 ms: 1.38x faster                                                             |
| unpickle_pure_python    | 203 us                                                 | 148 us: 1.38x faster                                                              |
| raytrace                | 328 ms                                                 | 240 ms: 1.36x faster                                                              |
| async_tree_none         | 402 ms                                                 | 295 ms: 1.36x faster                                                              |
| async_tree_io           | 1.02 sec                                               | 752 ms: 1.36x faster                                                              |
| chaos                   | 66.8 ms                                                | 49.3 ms: 1.35x faster                                                             |
| deepcopy_memo           | 34.5 us                                                | 25.8 us: 1.34x faster                                                             |
| pyflate                 | 453 ms                                                 | 341 ms: 1.33x faster                                                              |
| pycparser               | 915 ms                                                 | 695 ms: 1.32x faster                                                              |
| spectral_norm           | 96.4 ms                                                | 73.3 ms: 1.32x faster                                                             |
| json_dumps              | 8.38 ms                                                | 6.39 ms: 1.31x faster                                                             |
| tornado_http            | 91.9 ms                                                | 70.8 ms: 1.30x faster                                                             |
| float                   | 72.3 ms                                                | 56.2 ms: 1.29x faster                                                             |
| generators              | 32.9 ms                                                | 26.2 ms: 1.26x faster                                                             |
| genshi_text             | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                             |
| chameleon               | 5.84 ms                                                | 4.69 ms: 1.25x faster                                                             |
| genshi_xml              | 37.6 ms                                                | 30.3 ms: 1.24x faster                                                             |
| create_gc_cycles        | 876 us                                                 | 707 us: 1.24x faster                                                              |
| regex_compile           | 96.6 ms                                                | 78.5 ms: 1.23x faster                                                             |
| pprint_pformat          | 1.24 sec                                               | 1.01 sec: 1.23x faster                                                            |
| pprint_safe_repr        | 609 ms                                                 | 497 ms: 1.22x faster                                                              |
| async_tree_cpu_io_mixed | 670 ms                                                 | 548 ms: 1.22x faster                                                              |
| logging_simple          | 4.63 us                                                | 3.79 us: 1.22x faster                                                             |
| logging_format          | 5.01 us                                                | 4.11 us: 1.22x faster                                                             |
| django_template         | 27.3 ms                                                | 22.6 ms: 1.21x faster                                                             |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.48 ms: 1.21x faster                                                             |
| deepcopy                | 278 us                                                 | 231 us: 1.20x faster                                                              |
| dulwich_log             | 37.1 ms                                                | 30.9 ms: 1.20x faster                                                             |
| scimark_fft             | 232 ms                                                 | 194 ms: 1.19x faster                                                              |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.95 ms: 1.18x faster                                                             |
| xml_etree_process       | 45.1 ms                                                | 38.5 ms: 1.17x faster                                                             |
| thrift                  | 586 us                                                 | 501 us: 1.17x faster                                                              |
| html5lib                | 44.1 ms                                                | 37.7 ms: 1.17x faster                                                             |
| 2to3                    | 202 ms                                                 | 173 ms: 1.17x faster                                                              |
| deepcopy_reduce         | 2.38 us                                                | 2.05 us: 1.16x faster                                                             |
| docutils                | 1.78 sec                                               | 1.54 sec: 1.15x faster                                                            |
| unpack_sequence         | 38.7 ns                                                | 33.8 ns: 1.15x faster                                                             |
| mypy2                   | 308 ms                                                 | 271 ms: 1.14x faster                                                              |
| sqlglot_optimize        | 38.0 ms                                                | 33.7 ms: 1.13x faster                                                             |
| fannkuch                | 317 ms                                                 | 284 ms: 1.12x faster                                                              |
| sqlalchemy_declarative  | 74.8 ms                                                | 67.5 ms: 1.11x faster                                                             |
| bench_thread_pool       | 548 us                                                 | 497 us: 1.10x faster                                                              |
| sympy_integrate         | 13.4 ms                                                | 12.2 ms: 1.10x faster                                                             |
| json                    | 3.10 ms                                                | 2.83 ms: 1.09x faster                                                             |
| regex_v8                | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                             |
| mdp                     | 1.67 sec                                               | 1.56 sec: 1.07x faster                                                            |
| meteor_contest          | 78.6 ms                                                | 74.0 ms: 1.06x faster                                                             |
| sqlglot_normalize       | 197 ms                                                 | 185 ms: 1.06x faster                                                              |
| python_startup          | 12.6 ms                                                | 11.9 ms: 1.06x faster                                                             |
| coroutines              | 20.2 ms                                                | 19.1 ms: 1.06x faster                                                             |
| unpickle                | 9.77 us                                                | 9.27 us: 1.05x faster                                                             |
| regex_dna               | 160 ms                                                 | 152 ms: 1.05x faster                                                              |
| comprehensions          | 17.7 us                                                | 16.8 us: 1.05x faster                                                             |
| nqueens                 | 68.1 ms                                                | 65.7 ms: 1.04x faster                                                             |
| sympy_expand            | 276 ms                                                 | 267 ms: 1.03x faster                                                              |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                                             |
| pathlib                 | 28.8 ms                                                | 28.1 ms: 1.03x faster                                                             |
| xml_etree_parse         | 107 ms                                                 | 105 ms: 1.02x faster                                                              |
| sympy_str               | 169 ms                                                 | 166 ms: 1.02x faster                                                              |
| sympy_sum               | 94.3 ms                                                | 93.6 ms: 1.01x faster                                                             |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                                              |
| xml_etree_iterparse     | 72.6 ms                                                | 73.4 ms: 1.01x slower                                                             |
| python_startup_no_site  | 9.73 ms                                                | 9.92 ms: 1.02x slower                                                             |
| xml_etree_generate      | 54.3 ms                                                | 56.2 ms: 1.04x slower                                                             |
| pickle                  | 7.36 us                                                | 7.65 us: 1.04x slower                                                             |
| sqlite_synth            | 1.47 us                                                | 1.54 us: 1.05x slower                                                             |
| pickle_dict             | 17.8 us                                                | 18.7 us: 1.05x slower                                                             |
| gc_traversal            | 2.40 ms                                                | 2.59 ms: 1.08x slower                                                             |
| regex_effbot            | 2.45 ms                                                | 2.65 ms: 1.08x slower                                                             |
| unpickle_list           | 2.66 us                                                | 2.90 us: 1.09x slower                                                             |
| pickle_list             | 2.83 us                                                | 3.12 us: 1.10x slower                                                             |
| bench_mp_pool           | 41.0 ms                                                | 46.8 ms: 1.14x slower                                                             |
| dask                    | 258 ms                                                 | 330 ms: 1.28x slower                                                              |
| async_generators        | 233 ms                                                 | 301 ms: 1.29x slower                                                              |
| coverage                | 40.8 ms                                                | 58.8 ms: 1.44x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.17x faster                                                                      |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x

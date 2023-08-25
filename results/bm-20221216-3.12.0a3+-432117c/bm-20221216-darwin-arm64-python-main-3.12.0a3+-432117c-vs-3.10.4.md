
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 432117c
- commit date: 2022-12-16
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 184 ms: 1.10x faster                                   |
| chameleon      | 5.84 ms                                                | 4.29 ms: 1.36x faster                                  |
| docutils       | 1.78 sec                                               | 1.44 sec: 1.24x faster                                 |
| html5lib       | 44.1 ms                                                | 33.2 ms: 1.33x faster                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 62.3 ms: 1.51x faster                                  |
| float          | 72.3 ms                                                | 53.4 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 72.7 ms: 1.33x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.0 ms: 1.09x faster                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.71 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 197 us: 1.44x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.16 ms: 1.36x faster                                  |
| unpickle_pure_python | 203 us                                                 | 151 us: 1.35x faster                                   |
| xml_etree_process    | 45.1 ms                                                | 34.4 ms: 1.31x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 92.9 ms: 1.16x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 47.0 ms: 1.15x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 65.5 ms: 1.11x faster                                  |
| unpickle_list        | 2.66 us                                                | 2.56 us: 1.04x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| pickle_list          | 2.83 us                                                | 2.84 us: 1.00x slower                                  |
| unpickle             | 9.77 us                                                | 9.84 us: 1.01x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| pickle               | 7.36 us                                                | 7.55 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 9.29 ms: 1.36x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 7.34 ms: 1.32x faster                                  |
| Geometric mean         | (ref)                                                  | 1.34x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 6.96 ms: 1.51x faster                                  |
| genshi_xml      | 37.6 ms                                                | 28.2 ms: 1.33x faster                                  |
| genshi_text     | 18.4 ms                                                | 13.9 ms: 1.32x faster                                  |
| django_template | 27.3 ms                                                | 20.7 ms: 1.32x faster                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.51 ms: 2.05x faster                                  |
| logging_silent          | 119 ns                                                 | 62.7 ns: 1.90x faster                                  |
| richards                | 51.4 ms                                                | 29.2 ms: 1.76x faster                                  |
| scimark_sor             | 127 ms                                                 | 78.1 ms: 1.62x faster                                  |
| raytrace                | 328 ms                                                 | 203 ms: 1.62x faster                                   |
| scimark_lu              | 110 ms                                                 | 69.0 ms: 1.59x faster                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 46.1 ms: 1.57x faster                                  |
| go                      | 165 ms                                                 | 106 ms: 1.55x faster                                   |
| nbody                   | 94.1 ms                                                | 62.3 ms: 1.51x faster                                  |
| mako                    | 10.5 ms                                                | 6.96 ms: 1.51x faster                                  |
| async_tree_memoization  | 493 ms                                                 | 330 ms: 1.49x faster                                   |
| crypto_pyaes            | 78.0 ms                                                | 53.0 ms: 1.47x faster                                  |
| pickle_pure_python      | 284 us                                                 | 197 us: 1.44x faster                                   |
| pathlib                 | 28.8 ms                                                | 20.4 ms: 1.41x faster                                  |
| async_tree_none         | 402 ms                                                 | 285 ms: 1.41x faster                                   |
| pyflate                 | 453 ms                                                 | 324 ms: 1.40x faster                                   |
| async_tree_io           | 1.02 sec                                               | 732 ms: 1.39x faster                                   |
| chaos                   | 66.8 ms                                                | 48.6 ms: 1.38x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.59 ms: 1.38x faster                                  |
| pycparser               | 915 ms                                                 | 665 ms: 1.38x faster                                   |
| sqlglot_parse           | 1.33 ms                                                | 976 us: 1.36x faster                                   |
| chameleon               | 5.84 ms                                                | 4.29 ms: 1.36x faster                                  |
| json_dumps              | 8.38 ms                                                | 6.16 ms: 1.36x faster                                  |
| python_startup          | 12.6 ms                                                | 9.29 ms: 1.36x faster                                  |
| float                   | 72.3 ms                                                | 53.4 ms: 1.36x faster                                  |
| thrift                  | 586 us                                                 | 433 us: 1.35x faster                                   |
| sqlglot_transpile       | 1.54 ms                                                | 1.14 ms: 1.35x faster                                  |
| logging_simple          | 4.63 us                                                | 3.44 us: 1.35x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 151 us: 1.35x faster                                   |
| spectral_norm           | 96.4 ms                                                | 71.7 ms: 1.34x faster                                  |
| logging_format          | 5.01 us                                                | 3.74 us: 1.34x faster                                  |
| genshi_xml              | 37.6 ms                                                | 28.2 ms: 1.33x faster                                  |
| regex_compile           | 96.6 ms                                                | 72.7 ms: 1.33x faster                                  |
| html5lib                | 44.1 ms                                                | 33.2 ms: 1.33x faster                                  |
| genshi_text             | 18.4 ms                                                | 13.9 ms: 1.32x faster                                  |
| python_startup_no_site  | 9.73 ms                                                | 7.34 ms: 1.32x faster                                  |
| django_template         | 27.3 ms                                                | 20.7 ms: 1.32x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 34.4 ms: 1.31x faster                                  |
| dulwich_log             | 37.1 ms                                                | 28.4 ms: 1.31x faster                                  |
| pprint_pformat          | 1.24 sec                                               | 955 ms: 1.30x faster                                   |
| pprint_safe_repr        | 609 ms                                                 | 470 ms: 1.30x faster                                   |
| unpack_sequence         | 38.7 ns                                                | 30.4 ns: 1.27x faster                                  |
| deepcopy_memo           | 34.5 us                                                | 27.4 us: 1.26x faster                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.77 ms: 1.25x faster                                  |
| fannkuch                | 317 ms                                                 | 255 ms: 1.25x faster                                   |
| async_tree_cpu_io_mixed | 670 ms                                                 | 538 ms: 1.25x faster                                   |
| docutils                | 1.78 sec                                               | 1.44 sec: 1.24x faster                                 |
| sqlglot_optimize        | 38.0 ms                                                | 30.8 ms: 1.23x faster                                  |
| bench_thread_pool       | 548 us                                                 | 445 us: 1.23x faster                                   |
| deepcopy                | 278 us                                                 | 227 us: 1.22x faster                                   |
| deepcopy_reduce         | 2.38 us                                                | 1.95 us: 1.22x faster                                  |
| scimark_fft             | 232 ms                                                 | 193 ms: 1.20x faster                                   |
| sympy_integrate         | 13.4 ms                                                | 11.3 ms: 1.18x faster                                  |
| sqlglot_normalize       | 197 ms                                                 | 167 ms: 1.17x faster                                   |
| async_generators        | 233 ms                                                 | 201 ms: 1.16x faster                                   |
| coroutines              | 20.2 ms                                                | 17.4 ms: 1.16x faster                                  |
| xml_etree_parse         | 107 ms                                                 | 92.9 ms: 1.16x faster                                  |
| xml_etree_generate      | 54.3 ms                                                | 47.0 ms: 1.15x faster                                  |
| nqueens                 | 68.1 ms                                                | 59.3 ms: 1.15x faster                                  |
| sympy_expand            | 276 ms                                                 | 240 ms: 1.15x faster                                   |
| sympy_str               | 169 ms                                                 | 150 ms: 1.13x faster                                   |
| mdp                     | 1.67 sec                                               | 1.50 sec: 1.12x faster                                 |
| sympy_sum               | 94.3 ms                                                | 85.0 ms: 1.11x faster                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 65.5 ms: 1.11x faster                                  |
| 2to3                    | 202 ms                                                 | 184 ms: 1.10x faster                                   |
| telco                   | 3.68 ms                                                | 3.35 ms: 1.10x faster                                  |
| json                    | 3.10 ms                                                | 2.82 ms: 1.10x faster                                  |
| regex_v8                | 17.5 ms                                                | 16.0 ms: 1.09x faster                                  |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| meteor_contest          | 78.6 ms                                                | 75.4 ms: 1.04x faster                                  |
| unpickle_list           | 2.66 us                                                | 2.56 us: 1.04x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.43 us: 1.03x faster                                  |
| generators              | 32.9 ms                                                | 32.2 ms: 1.02x faster                                  |
| pickle_list             | 2.83 us                                                | 2.84 us: 1.00x slower                                  |
| unpickle                | 9.77 us                                                | 9.84 us: 1.01x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| pickle                  | 7.36 us                                                | 7.55 us: 1.03x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 43.9 ms: 1.07x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.71 ms: 1.11x slower                                  |
| coverage                | 40.8 ms                                                | 54.9 ms: 1.35x slower                                  |
| Geometric mean          | (ref)                                                  | 1.26x faster                                           |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221216-3.12.0a3+-432117c/bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x


# Results vs. 3.10.4

- fork: python
- ref: f9774e57d84162ff0cba
- machine: darwin-arm64
- commit hash: f9774e5
- commit date: 2023-03-07
- overall geometric mean: 1.20x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 165 ms: 1.23x faster                                                  |
| chameleon      | 5.84 ms                                                | 4.48 ms: 1.30x faster                                                 |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.20x faster                                                |
| html5lib       | 44.1 ms                                                | 35.4 ms: 1.24x faster                                                 |
| tornado_http   | 91.9 ms                                                | 70.0 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 66.1 ms: 1.42x faster                                                 |
| float          | 72.3 ms                                                | 53.5 ms: 1.35x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.4 ms: 1.28x faster                                                 |
| regex_v8       | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                 |
| regex_dna      | 160 ms                                                 | 153 ms: 1.04x faster                                                  |
| regex_effbot   | 2.45 ms                                                | 2.69 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 191 us: 1.49x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                                  |
| json_dumps           | 8.38 ms                                                | 6.18 ms: 1.36x faster                                                 |
| xml_etree_process    | 45.1 ms                                                | 37.0 ms: 1.22x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 97.9 ms: 1.10x faster                                                 |
| xml_etree_generate   | 54.3 ms                                                | 51.1 ms: 1.06x faster                                                 |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 71.1 ms: 1.02x faster                                                 |
| unpickle_list        | 2.66 us                                                | 2.65 us: 1.01x faster                                                 |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle               | 7.36 us                                                | 7.47 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 9.73 ms                                                | 10.4 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.44 ms: 1.41x faster                                                 |
| genshi_xml      | 37.6 ms                                                | 29.2 ms: 1.29x faster                                                 |
| django_template | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                 |
| genshi_text     | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.59 ms: 1.99x faster                                                 |
| logging_silent          | 119 ns                                                 | 69.3 ns: 1.72x faster                                                 |
| richards                | 51.4 ms                                                | 30.5 ms: 1.68x faster                                                 |
| go                      | 165 ms                                                 | 111 ms: 1.49x faster                                                  |
| pickle_pure_python      | 284 us                                                 | 191 us: 1.49x faster                                                  |
| scimark_lu              | 110 ms                                                 | 74.2 ms: 1.48x faster                                                 |
| async_tree_memoization  | 493 ms                                                 | 336 ms: 1.47x faster                                                  |
| crypto_pyaes            | 78.0 ms                                                | 53.5 ms: 1.46x faster                                                 |
| scimark_sor             | 127 ms                                                 | 87.7 ms: 1.44x faster                                                 |
| raytrace                | 328 ms                                                 | 229 ms: 1.43x faster                                                  |
| nbody                   | 94.1 ms                                                | 66.1 ms: 1.42x faster                                                 |
| asyncio_tcp             | 673 ms                                                 | 473 ms: 1.42x faster                                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 51.0 ms: 1.42x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.46 ms: 1.42x faster                                                 |
| mako                    | 10.5 ms                                                | 7.44 ms: 1.41x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 145 us: 1.40x faster                                                  |
| chaos                   | 66.8 ms                                                | 47.8 ms: 1.40x faster                                                 |
| async_tree_none         | 402 ms                                                 | 289 ms: 1.39x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 744 ms: 1.37x faster                                                  |
| pyflate                 | 453 ms                                                 | 331 ms: 1.37x faster                                                  |
| pycparser               | 915 ms                                                 | 674 ms: 1.36x faster                                                  |
| json_dumps              | 8.38 ms                                                | 6.18 ms: 1.36x faster                                                 |
| float                   | 72.3 ms                                                | 53.5 ms: 1.35x faster                                                 |
| tornado_http            | 91.9 ms                                                | 70.0 ms: 1.31x faster                                                 |
| deepcopy_memo           | 34.5 us                                                | 26.4 us: 1.31x faster                                                 |
| chameleon               | 5.84 ms                                                | 4.48 ms: 1.30x faster                                                 |
| thrift                  | 586 us                                                 | 453 us: 1.29x faster                                                  |
| spectral_norm           | 96.4 ms                                                | 74.9 ms: 1.29x faster                                                 |
| genshi_xml              | 37.6 ms                                                | 29.2 ms: 1.29x faster                                                 |
| regex_compile           | 96.6 ms                                                | 75.4 ms: 1.28x faster                                                 |
| pprint_pformat          | 1.24 sec                                               | 970 ms: 1.28x faster                                                  |
| pprint_safe_repr        | 609 ms                                                 | 477 ms: 1.28x faster                                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.05 ms: 1.27x faster                                                 |
| logging_format          | 5.01 us                                                | 3.95 us: 1.27x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.66 us: 1.27x faster                                                 |
| django_template         | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                 |
| sqlglot_transpile       | 1.54 ms                                                | 1.22 ms: 1.26x faster                                                 |
| genshi_text             | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 29.6 ms: 1.25x faster                                                 |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.21 ms: 1.25x faster                                                 |
| deepcopy                | 278 us                                                 | 222 us: 1.25x faster                                                  |
| create_gc_cycles        | 876 us                                                 | 702 us: 1.25x faster                                                  |
| html5lib                | 44.1 ms                                                | 35.4 ms: 1.24x faster                                                 |
| 2to3                    | 202 ms                                                 | 165 ms: 1.23x faster                                                  |
| fannkuch                | 317 ms                                                 | 258 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 547 ms: 1.22x faster                                                  |
| deepcopy_reduce         | 2.38 us                                                | 1.95 us: 1.22x faster                                                 |
| xml_etree_process       | 45.1 ms                                                | 37.0 ms: 1.22x faster                                                 |
| docutils                | 1.78 sec                                               | 1.49 sec: 1.20x faster                                                |
| scimark_fft             | 232 ms                                                 | 196 ms: 1.19x faster                                                  |
| generators              | 32.9 ms                                                | 27.9 ms: 1.18x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.1 ms: 1.18x faster                                                 |
| mypy2                   | 308 ms                                                 | 262 ms: 1.18x faster                                                  |
| unpack_sequence         | 38.7 ns                                                | 32.9 ns: 1.17x faster                                                 |
| sqlalchemy_declarative  | 74.8 ms                                                | 63.8 ms: 1.17x faster                                                 |
| bench_thread_pool       | 548 us                                                 | 472 us: 1.16x faster                                                  |
| sympy_integrate         | 13.4 ms                                                | 11.7 ms: 1.15x faster                                                 |
| sqlglot_normalize       | 197 ms                                                 | 175 ms: 1.12x faster                                                  |
| mdp                     | 1.67 sec                                               | 1.50 sec: 1.12x faster                                                |
| coroutines              | 20.2 ms                                                | 18.1 ms: 1.11x faster                                                 |
| sympy_expand            | 276 ms                                                 | 248 ms: 1.11x faster                                                  |
| json                    | 3.10 ms                                                | 2.79 ms: 1.11x faster                                                 |
| xml_etree_parse         | 107 ms                                                 | 97.9 ms: 1.10x faster                                                 |
| scimark_sparse_mat_mult | 3.47 ms                                                | 3.17 ms: 1.10x faster                                                 |
| sympy_str               | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| regex_v8                | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                 |
| nqueens                 | 68.1 ms                                                | 63.1 ms: 1.08x faster                                                 |
| meteor_contest          | 78.6 ms                                                | 72.9 ms: 1.08x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.37 us: 1.08x faster                                                 |
| sympy_sum               | 94.3 ms                                                | 88.2 ms: 1.07x faster                                                 |
| xml_etree_generate      | 54.3 ms                                                | 51.1 ms: 1.06x faster                                                 |
| telco                   | 3.68 ms                                                | 3.49 ms: 1.05x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                 |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| regex_dna               | 160 ms                                                 | 153 ms: 1.04x faster                                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 71.1 ms: 1.02x faster                                                 |
| python_startup          | 12.6 ms                                                | 12.5 ms: 1.01x faster                                                 |
| unpickle_list           | 2.66 us                                                | 2.65 us: 1.01x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| gc_traversal            | 2.40 ms                                                | 2.43 ms: 1.01x slower                                                 |
| pickle                  | 7.36 us                                                | 7.47 us: 1.02x slower                                                 |
| python_startup_no_site  | 9.73 ms                                                | 10.4 ms: 1.07x slower                                                 |
| regex_effbot            | 2.45 ms                                                | 2.69 ms: 1.10x slower                                                 |
| bench_mp_pool           | 41.0 ms                                                | 46.5 ms: 1.14x slower                                                 |
| async_generators        | 233 ms                                                 | 272 ms: 1.16x slower                                                  |
| dask                    | 258 ms                                                 | 325 ms: 1.26x slower                                                  |
| coverage                | 40.8 ms                                                | 59.6 ms: 1.46x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (3): unpickle, comprehensions, pickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

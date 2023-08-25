
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 0fd3891
- commit date: 2023-04-22
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-darwin-arm64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 161 ms: 1.26x faster                                   |
| chameleon      | 5.84 ms                                                | 4.42 ms: 1.32x faster                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                 |
| html5lib       | 44.1 ms                                                | 35.1 ms: 1.26x faster                                  |
| tornado_http   | 91.9 ms                                                | 69.8 ms: 1.32x faster                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-darwin-arm64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 61.3 ms: 1.54x faster                                  |
| float          | 72.3 ms                                                | 53.0 ms: 1.36x faster                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-darwin-arm64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 70.8 ms: 1.36x faster                                  |
| regex_v8       | 17.5 ms                                                | 15.9 ms: 1.10x faster                                  |
| regex_dna      | 160 ms                                                 | 151 ms: 1.06x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.65 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-darwin-arm64-python-main-3.12.0a7+-0fd3891 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 184 us: 1.54x faster                                   |
| unpickle_pure_python | 203 us                                                 | 144 us: 1.41x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.08 ms: 1.38x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 35.7 ms: 1.26x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 98.4 ms: 1.09x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 51.0 ms: 1.06x faster                                  |
| unpickle             | 9.77 us                                                | 9.29 us: 1.05x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 69.2 ms: 1.05x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| unpickle_list        | 2.66 us                                                | 2.64 us: 1.01x faster                                  |
| pickle_list          | 2.83 us                                                | 2.89 us: 1.02x slower                                  |
| pickle               | 7.36 us                                                | 7.55 us: 1.03x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.4 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-darwin-arm64-python-main-3.12.0a7+-0fd3891 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup | 12.6 ms                                                | 11.8 ms: 1.07x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-darwin-arm64-python-main-3.12.0a7+-0fd3891 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.53 ms: 1.39x faster                                  |
| django_template | 27.3 ms                                                | 19.9 ms: 1.37x faster                                  |
| genshi_text     | 18.4 ms                                                | 13.8 ms: 1.34x faster                                  |
| genshi_xml      | 37.6 ms                                                | 28.3 ms: 1.33x faster                                  |
| Geometric mean  | (ref)                                                  | 1.36x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-darwin-arm64-python-main-3.12.0a7+-0fd3891 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.44 ms: 2.11x faster                                  |
| logging_silent          | 119 ns                                                 | 67.4 ns: 1.77x faster                                  |
| richards                | 51.4 ms                                                | 30.7 ms: 1.68x faster                                  |
| scimark_sor             | 127 ms                                                 | 79.2 ms: 1.60x faster                                  |
| sqlglot_parse           | 1.33 ms                                                | 838 us: 1.59x faster                                   |
| go                      | 165 ms                                                 | 106 ms: 1.55x faster                                   |
| async_tree_memoization  | 493 ms                                                 | 318 ms: 1.55x faster                                   |
| sqlglot_transpile       | 1.54 ms                                                | 998 us: 1.54x faster                                   |
| pickle_pure_python      | 284 us                                                 | 184 us: 1.54x faster                                   |
| nbody                   | 94.1 ms                                                | 61.3 ms: 1.54x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.13 ms: 1.53x faster                                  |
| chaos                   | 66.8 ms                                                | 44.1 ms: 1.52x faster                                  |
| scimark_lu              | 110 ms                                                 | 72.5 ms: 1.52x faster                                  |
| raytrace                | 328 ms                                                 | 220 ms: 1.49x faster                                   |
| crypto_pyaes            | 78.0 ms                                                | 53.0 ms: 1.47x faster                                  |
| asyncio_tcp             | 673 ms                                                 | 458 ms: 1.47x faster                                   |
| scimark_monte_carlo     | 72.2 ms                                                | 49.5 ms: 1.46x faster                                  |
| async_tree_none         | 402 ms                                                 | 276 ms: 1.46x faster                                   |
| async_tree_io           | 1.02 sec                                               | 710 ms: 1.44x faster                                   |
| unpickle_pure_python    | 203 us                                                 | 144 us: 1.41x faster                                   |
| pycparser               | 915 ms                                                 | 654 ms: 1.40x faster                                   |
| mako                    | 10.5 ms                                                | 7.53 ms: 1.39x faster                                  |
| pyflate                 | 453 ms                                                 | 326 ms: 1.39x faster                                   |
| unpack_sequence         | 38.7 ns                                                | 27.9 ns: 1.38x faster                                  |
| json_dumps              | 8.38 ms                                                | 6.08 ms: 1.38x faster                                  |
| django_template         | 27.3 ms                                                | 19.9 ms: 1.37x faster                                  |
| regex_compile           | 96.6 ms                                                | 70.8 ms: 1.36x faster                                  |
| float                   | 72.3 ms                                                | 53.0 ms: 1.36x faster                                  |
| logging_format          | 5.01 us                                                | 3.67 us: 1.36x faster                                  |
| logging_simple          | 4.63 us                                                | 3.40 us: 1.36x faster                                  |
| pprint_pformat          | 1.24 sec                                               | 914 ms: 1.36x faster                                   |
| pprint_safe_repr        | 609 ms                                                 | 449 ms: 1.36x faster                                   |
| spectral_norm           | 96.4 ms                                                | 71.4 ms: 1.35x faster                                  |
| deepcopy_memo           | 34.5 us                                                | 25.6 us: 1.35x faster                                  |
| generators              | 32.9 ms                                                | 24.6 ms: 1.34x faster                                  |
| genshi_text             | 18.4 ms                                                | 13.8 ms: 1.34x faster                                  |
| fannkuch                | 317 ms                                                 | 238 ms: 1.34x faster                                   |
| genshi_xml              | 37.6 ms                                                | 28.3 ms: 1.33x faster                                  |
| chameleon               | 5.84 ms                                                | 4.42 ms: 1.32x faster                                  |
| tornado_http            | 91.9 ms                                                | 69.8 ms: 1.32x faster                                  |
| sqlalchemy_imperative   | 9.03 ms                                                | 6.88 ms: 1.31x faster                                  |
| thrift                  | 586 us                                                 | 450 us: 1.30x faster                                   |
| dulwich_log             | 37.1 ms                                                | 28.6 ms: 1.30x faster                                  |
| deepcopy                | 278 us                                                 | 215 us: 1.29x faster                                   |
| create_gc_cycles        | 876 us                                                 | 688 us: 1.27x faster                                   |
| deepcopy_reduce         | 2.38 us                                                | 1.88 us: 1.27x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 35.7 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 531 ms: 1.26x faster                                   |
| 2to3                    | 202 ms                                                 | 161 ms: 1.26x faster                                   |
| html5lib                | 44.1 ms                                                | 35.1 ms: 1.26x faster                                  |
| scimark_fft             | 232 ms                                                 | 188 ms: 1.23x faster                                   |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.3 ms: 1.21x faster                                  |
| nqueens                 | 68.1 ms                                                | 56.4 ms: 1.21x faster                                  |
| sqlalchemy_declarative  | 74.8 ms                                                | 62.0 ms: 1.21x faster                                  |
| mypy2                   | 308 ms                                                 | 258 ms: 1.20x faster                                   |
| bench_thread_pool       | 548 us                                                 | 459 us: 1.20x faster                                   |
| pylint                  | 307 ms                                                 | 259 ms: 1.19x faster                                   |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.94 ms: 1.18x faster                                  |
| sympy_integrate         | 13.4 ms                                                | 11.4 ms: 1.17x faster                                  |
| coroutines              | 20.2 ms                                                | 17.3 ms: 1.17x faster                                  |
| sympy_expand            | 276 ms                                                 | 237 ms: 1.16x faster                                   |
| sqlglot_normalize       | 197 ms                                                 | 170 ms: 1.16x faster                                   |
| sympy_str               | 169 ms                                                 | 147 ms: 1.15x faster                                   |
| sympy_sum               | 94.3 ms                                                | 84.9 ms: 1.11x faster                                  |
| mdp                     | 1.67 sec                                               | 1.51 sec: 1.11x faster                                 |
| regex_v8                | 17.5 ms                                                | 15.9 ms: 1.10x faster                                  |
| comprehensions          | 17.7 us                                                | 16.1 us: 1.10x faster                                  |
| json                    | 3.10 ms                                                | 2.82 ms: 1.10x faster                                  |
| xml_etree_parse         | 107 ms                                                 | 98.4 ms: 1.09x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.08x faster                                  |
| pathlib                 | 28.8 ms                                                | 26.7 ms: 1.08x faster                                  |
| telco                   | 3.68 ms                                                | 3.42 ms: 1.07x faster                                  |
| python_startup          | 12.6 ms                                                | 11.8 ms: 1.07x faster                                  |
| xml_etree_generate      | 54.3 ms                                                | 51.0 ms: 1.06x faster                                  |
| regex_dna               | 160 ms                                                 | 151 ms: 1.06x faster                                   |
| meteor_contest          | 78.6 ms                                                | 74.6 ms: 1.05x faster                                  |
| unpickle                | 9.77 us                                                | 9.29 us: 1.05x faster                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 69.2 ms: 1.05x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| unpickle_list           | 2.66 us                                                | 2.64 us: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| gc_traversal            | 2.40 ms                                                | 2.42 ms: 1.01x slower                                  |
| pickle_list             | 2.83 us                                                | 2.89 us: 1.02x slower                                  |
| pickle                  | 7.36 us                                                | 7.55 us: 1.03x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.4 us: 1.04x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.65 ms: 1.08x slower                                  |
| async_generators        | 233 ms                                                 | 265 ms: 1.14x slower                                   |
| bench_mp_pool           | 41.0 ms                                                | 46.8 ms: 1.14x slower                                  |
| dask                    | 258 ms                                                 | 310 ms: 1.20x slower                                   |
| coverage                | 40.8 ms                                                | 51.7 ms: 1.27x slower                                  |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

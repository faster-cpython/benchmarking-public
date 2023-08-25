
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 61f1e67
- commit date: 2023-02-18
- overall geometric mean: 1.22x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 161 ms: 1.26x faster                                   |
| chameleon      | 5.84 ms                                                | 4.45 ms: 1.31x faster                                  |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.21x faster                                 |
| html5lib       | 44.1 ms                                                | 35.5 ms: 1.24x faster                                  |
| tornado_http   | 91.9 ms                                                | 70.2 ms: 1.31x faster                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 64.1 ms: 1.47x faster                                  |
| float          | 72.3 ms                                                | 52.4 ms: 1.38x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 72.9 ms: 1.33x faster                                  |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.60 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 193 us: 1.47x faster                                   |
| unpickle_pure_python | 203 us                                                 | 142 us: 1.43x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.16 ms: 1.36x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 35.9 ms: 1.25x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 96.6 ms: 1.11x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 50.2 ms: 1.08x faster                                  |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 69.8 ms: 1.04x faster                                  |
| unpickle_list        | 2.66 us                                                | 2.56 us: 1.04x faster                                  |
| pickle_list          | 2.83 us                                                | 2.80 us: 1.01x faster                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| pickle               | 7.36 us                                                | 7.50 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.4 ms: 1.11x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 9.34 ms: 1.04x faster                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.35 ms: 1.43x faster                                  |
| genshi_xml      | 37.6 ms                                                | 28.2 ms: 1.33x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| django_template | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| Geometric mean  | (ref)                                                  | 1.33x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.56 ms: 2.01x faster                                  |
| logging_silent          | 119 ns                                                 | 66.0 ns: 1.80x faster                                  |
| richards                | 51.4 ms                                                | 29.9 ms: 1.72x faster                                  |
| go                      | 165 ms                                                 | 108 ms: 1.52x faster                                   |
| async_tree_memoization  | 493 ms                                                 | 325 ms: 1.52x faster                                   |
| scimark_lu              | 110 ms                                                 | 72.7 ms: 1.51x faster                                  |
| asyncio_tcp             | 673 ms                                                 | 456 ms: 1.48x faster                                   |
| scimark_sor             | 127 ms                                                 | 85.9 ms: 1.48x faster                                  |
| raytrace                | 328 ms                                                 | 223 ms: 1.47x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.30 ms: 1.47x faster                                  |
| pickle_pure_python      | 284 us                                                 | 193 us: 1.47x faster                                   |
| nbody                   | 94.1 ms                                                | 64.1 ms: 1.47x faster                                  |
| crypto_pyaes            | 78.0 ms                                                | 53.5 ms: 1.46x faster                                  |
| chaos                   | 66.8 ms                                                | 46.5 ms: 1.44x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 142 us: 1.43x faster                                   |
| mako                    | 10.5 ms                                                | 7.35 ms: 1.43x faster                                  |
| async_tree_none         | 402 ms                                                 | 283 ms: 1.42x faster                                   |
| pyflate                 | 453 ms                                                 | 325 ms: 1.40x faster                                   |
| async_tree_io           | 1.02 sec                                               | 736 ms: 1.38x faster                                   |
| pycparser               | 915 ms                                                 | 662 ms: 1.38x faster                                   |
| float                   | 72.3 ms                                                | 52.4 ms: 1.38x faster                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 52.4 ms: 1.38x faster                                  |
| deepcopy_memo           | 34.5 us                                                | 25.3 us: 1.36x faster                                  |
| json_dumps              | 8.38 ms                                                | 6.16 ms: 1.36x faster                                  |
| genshi_xml              | 37.6 ms                                                | 28.2 ms: 1.33x faster                                  |
| regex_compile           | 96.6 ms                                                | 72.9 ms: 1.33x faster                                  |
| chameleon               | 5.84 ms                                                | 4.45 ms: 1.31x faster                                  |
| tornado_http            | 91.9 ms                                                | 70.2 ms: 1.31x faster                                  |
| pprint_safe_repr        | 609 ms                                                 | 470 ms: 1.29x faster                                   |
| pprint_pformat          | 1.24 sec                                               | 959 ms: 1.29x faster                                   |
| genshi_text             | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| generators              | 32.9 ms                                                | 25.5 ms: 1.29x faster                                  |
| logging_format          | 5.01 us                                                | 3.89 us: 1.29x faster                                  |
| django_template         | 27.3 ms                                                | 21.3 ms: 1.28x faster                                  |
| spectral_norm           | 96.4 ms                                                | 75.2 ms: 1.28x faster                                  |
| logging_simple          | 4.63 us                                                | 3.61 us: 1.28x faster                                  |
| thrift                  | 586 us                                                 | 458 us: 1.28x faster                                   |
| sqlglot_parse           | 1.33 ms                                                | 1.05 ms: 1.27x faster                                  |
| deepcopy                | 278 us                                                 | 220 us: 1.26x faster                                   |
| sqlglot_transpile       | 1.54 ms                                                | 1.22 ms: 1.26x faster                                  |
| dulwich_log             | 37.1 ms                                                | 29.5 ms: 1.26x faster                                  |
| 2to3                    | 202 ms                                                 | 161 ms: 1.26x faster                                   |
| xml_etree_process       | 45.1 ms                                                | 35.9 ms: 1.25x faster                                  |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.24 ms: 1.25x faster                                  |
| create_gc_cycles        | 876 us                                                 | 704 us: 1.24x faster                                   |
| html5lib                | 44.1 ms                                                | 35.5 ms: 1.24x faster                                  |
| fannkuch                | 317 ms                                                 | 255 ms: 1.24x faster                                   |
| async_tree_cpu_io_mixed | 670 ms                                                 | 541 ms: 1.24x faster                                   |
| deepcopy_reduce         | 2.38 us                                                | 1.93 us: 1.24x faster                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.81 ms: 1.23x faster                                  |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.21x faster                                 |
| scimark_fft             | 232 ms                                                 | 193 ms: 1.20x faster                                   |
| mypy2                   | 308 ms                                                 | 257 ms: 1.20x faster                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.8 ms: 1.20x faster                                  |
| unpack_sequence         | 38.7 ns                                                | 32.7 ns: 1.18x faster                                  |
| bench_thread_pool       | 548 us                                                 | 463 us: 1.18x faster                                   |
| sqlalchemy_declarative  | 74.8 ms                                                | 63.4 ms: 1.18x faster                                  |
| sympy_integrate         | 13.4 ms                                                | 11.3 ms: 1.18x faster                                  |
| sympy_str               | 169 ms                                                 | 147 ms: 1.15x faster                                   |
| coroutines              | 20.2 ms                                                | 17.7 ms: 1.14x faster                                  |
| sympy_expand            | 276 ms                                                 | 243 ms: 1.13x faster                                   |
| sqlglot_normalize       | 197 ms                                                 | 173 ms: 1.13x faster                                   |
| sympy_sum               | 94.3 ms                                                | 83.5 ms: 1.13x faster                                  |
| json                    | 3.10 ms                                                | 2.77 ms: 1.12x faster                                  |
| regex_v8                | 17.5 ms                                                | 15.7 ms: 1.12x faster                                  |
| nqueens                 | 68.1 ms                                                | 61.1 ms: 1.11x faster                                  |
| xml_etree_parse         | 107 ms                                                 | 96.6 ms: 1.11x faster                                  |
| python_startup          | 12.6 ms                                                | 11.4 ms: 1.11x faster                                  |
| mdp                     | 1.67 sec                                               | 1.53 sec: 1.09x faster                                 |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.09x faster                                  |
| xml_etree_generate      | 54.3 ms                                                | 50.2 ms: 1.08x faster                                  |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| telco                   | 3.68 ms                                                | 3.47 ms: 1.06x faster                                  |
| pathlib                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                  |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 69.8 ms: 1.04x faster                                  |
| python_startup_no_site  | 9.73 ms                                                | 9.34 ms: 1.04x faster                                  |
| unpickle_list           | 2.66 us                                                | 2.56 us: 1.04x faster                                  |
| meteor_contest          | 78.6 ms                                                | 75.8 ms: 1.04x faster                                  |
| pickle_list             | 2.83 us                                                | 2.80 us: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                   |
| gc_traversal            | 2.40 ms                                                | 2.42 ms: 1.01x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| pickle                  | 7.36 us                                                | 7.50 us: 1.02x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.60 ms: 1.06x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 45.0 ms: 1.10x slower                                  |
| async_generators        | 233 ms                                                 | 263 ms: 1.13x slower                                   |
| dask                    | 258 ms                                                 | 318 ms: 1.24x slower                                   |
| coverage                | 40.8 ms                                                | 61.0 ms: 1.49x slower                                  |
| Geometric mean          | (ref)                                                  | 1.22x faster                                           |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.19x

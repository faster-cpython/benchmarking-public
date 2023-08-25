
# Results vs. 3.10.4

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: darwin-arm64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 181 ms: 1.12x faster                                                       |
| chameleon      | 5.84 ms                                                | 4.58 ms: 1.28x faster                                                      |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                     |
| html5lib       | 44.1 ms                                                | 34.9 ms: 1.26x faster                                                      |
| tornado_http   | 91.9 ms                                                | 70.2 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                  | 1.24x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 64.4 ms: 1.46x faster                                                      |
| float          | 72.3 ms                                                | 52.4 ms: 1.38x faster                                                      |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 73.6 ms: 1.31x faster                                                      |
| regex_v8       | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                      |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                                       |
| regex_effbot   | 2.45 ms                                                | 2.61 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 194 us: 1.46x faster                                                       |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                                       |
| json_dumps           | 8.38 ms                                                | 6.15 ms: 1.36x faster                                                      |
| xml_etree_process    | 45.1 ms                                                | 35.4 ms: 1.27x faster                                                      |
| xml_etree_parse      | 107 ms                                                 | 94.8 ms: 1.13x faster                                                      |
| xml_etree_generate   | 54.3 ms                                                | 49.3 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 72.6 ms                                                | 68.3 ms: 1.06x faster                                                      |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                      |
| unpickle             | 9.77 us                                                | 9.87 us: 1.01x slower                                                      |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                                      |
| unpickle_list        | 2.66 us                                                | 2.71 us: 1.02x slower                                                      |
| pickle               | 7.36 us                                                | 7.55 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                      |
| python_startup_no_site | 9.73 ms                                                | 7.38 ms: 1.32x faster                                                      |
| Geometric mean         | (ref)                                                  | 1.33x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.29 ms: 1.44x faster                                                      |
| genshi_xml      | 37.6 ms                                                | 28.9 ms: 1.30x faster                                                      |
| django_template | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                      |
| genshi_text     | 18.4 ms                                                | 14.8 ms: 1.25x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.59 ms: 1.99x faster                                                      |
| logging_silent          | 119 ns                                                 | 66.0 ns: 1.80x faster                                                      |
| asyncio_tcp             | 673 ms                                                 | 395 ms: 1.70x faster                                                       |
| richards                | 51.4 ms                                                | 30.7 ms: 1.67x faster                                                      |
| scimark_monte_carlo     | 72.2 ms                                                | 45.7 ms: 1.58x faster                                                      |
| raytrace                | 328 ms                                                 | 210 ms: 1.56x faster                                                       |
| scimark_lu              | 110 ms                                                 | 71.5 ms: 1.54x faster                                                      |
| go                      | 165 ms                                                 | 109 ms: 1.51x faster                                                       |
| crypto_pyaes            | 78.0 ms                                                | 52.1 ms: 1.50x faster                                                      |
| async_tree_memoization  | 493 ms                                                 | 332 ms: 1.49x faster                                                       |
| scimark_sor             | 127 ms                                                 | 85.2 ms: 1.49x faster                                                      |
| nbody                   | 94.1 ms                                                | 64.4 ms: 1.46x faster                                                      |
| pickle_pure_python      | 284 us                                                 | 194 us: 1.46x faster                                                       |
| mako                    | 10.5 ms                                                | 7.29 ms: 1.44x faster                                                      |
| pyflate                 | 453 ms                                                 | 322 ms: 1.41x faster                                                       |
| unpickle_pure_python    | 203 us                                                 | 145 us: 1.40x faster                                                       |
| async_tree_none         | 402 ms                                                 | 288 ms: 1.40x faster                                                       |
| chaos                   | 66.8 ms                                                | 48.1 ms: 1.39x faster                                                      |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.39x faster                                                      |
| float                   | 72.3 ms                                                | 52.4 ms: 1.38x faster                                                      |
| async_tree_io           | 1.02 sec                                               | 743 ms: 1.37x faster                                                       |
| json_dumps              | 8.38 ms                                                | 6.15 ms: 1.36x faster                                                      |
| pycparser               | 915 ms                                                 | 680 ms: 1.35x faster                                                       |
| hexiom                  | 6.32 ms                                                | 4.71 ms: 1.34x faster                                                      |
| python_startup          | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                      |
| spectral_norm           | 96.4 ms                                                | 72.8 ms: 1.32x faster                                                      |
| deepcopy_memo           | 34.5 us                                                | 26.1 us: 1.32x faster                                                      |
| thrift                  | 586 us                                                 | 444 us: 1.32x faster                                                       |
| python_startup_no_site  | 9.73 ms                                                | 7.38 ms: 1.32x faster                                                      |
| pprint_safe_repr        | 609 ms                                                 | 462 ms: 1.32x faster                                                       |
| pprint_pformat          | 1.24 sec                                               | 941 ms: 1.32x faster                                                       |
| sqlglot_parse           | 1.33 ms                                                | 1.01 ms: 1.31x faster                                                      |
| regex_compile           | 96.6 ms                                                | 73.6 ms: 1.31x faster                                                      |
| tornado_http            | 91.9 ms                                                | 70.2 ms: 1.31x faster                                                      |
| sqlglot_transpile       | 1.54 ms                                                | 1.18 ms: 1.30x faster                                                      |
| dulwich_log             | 37.1 ms                                                | 28.5 ms: 1.30x faster                                                      |
| genshi_xml              | 37.6 ms                                                | 28.9 ms: 1.30x faster                                                      |
| logging_format          | 5.01 us                                                | 3.87 us: 1.30x faster                                                      |
| django_template         | 27.3 ms                                                | 21.1 ms: 1.29x faster                                                      |
| logging_simple          | 4.63 us                                                | 3.60 us: 1.29x faster                                                      |
| chameleon               | 5.84 ms                                                | 4.58 ms: 1.28x faster                                                      |
| xml_etree_process       | 45.1 ms                                                | 35.4 ms: 1.27x faster                                                      |
| html5lib                | 44.1 ms                                                | 34.9 ms: 1.26x faster                                                      |
| deepcopy                | 278 us                                                 | 220 us: 1.26x faster                                                       |
| genshi_text             | 18.4 ms                                                | 14.8 ms: 1.25x faster                                                      |
| fannkuch                | 317 ms                                                 | 255 ms: 1.24x faster                                                       |
| deepcopy_reduce         | 2.38 us                                                | 1.92 us: 1.24x faster                                                      |
| create_gc_cycles        | 876 us                                                 | 711 us: 1.23x faster                                                       |
| async_tree_cpu_io_mixed | 670 ms                                                 | 544 ms: 1.23x faster                                                       |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                     |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.83 ms: 1.23x faster                                                      |
| bench_thread_pool       | 548 us                                                 | 447 us: 1.23x faster                                                       |
| scimark_fft             | 232 ms                                                 | 193 ms: 1.20x faster                                                       |
| sympy_integrate         | 13.4 ms                                                | 11.2 ms: 1.20x faster                                                      |
| sqlglot_optimize        | 38.0 ms                                                | 31.7 ms: 1.20x faster                                                      |
| sympy_str               | 169 ms                                                 | 145 ms: 1.17x faster                                                       |
| async_generators        | 233 ms                                                 | 200 ms: 1.16x faster                                                       |
| unpack_sequence         | 38.7 ns                                                | 33.6 ns: 1.15x faster                                                      |
| sympy_sum               | 94.3 ms                                                | 82.0 ms: 1.15x faster                                                      |
| sympy_expand            | 276 ms                                                 | 241 ms: 1.15x faster                                                       |
| nqueens                 | 68.1 ms                                                | 59.7 ms: 1.14x faster                                                      |
| xml_etree_parse         | 107 ms                                                 | 94.8 ms: 1.13x faster                                                      |
| sqlglot_normalize       | 197 ms                                                 | 174 ms: 1.13x faster                                                       |
| 2to3                    | 202 ms                                                 | 181 ms: 1.12x faster                                                       |
| xml_etree_generate      | 54.3 ms                                                | 49.3 ms: 1.10x faster                                                      |
| mdp                     | 1.67 sec                                               | 1.52 sec: 1.10x faster                                                     |
| json                    | 3.10 ms                                                | 2.84 ms: 1.09x faster                                                      |
| regex_v8                | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                      |
| telco                   | 3.68 ms                                                | 3.39 ms: 1.09x faster                                                      |
| coroutines              | 20.2 ms                                                | 18.6 ms: 1.08x faster                                                      |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.08x faster                                                      |
| meteor_contest          | 78.6 ms                                                | 73.0 ms: 1.08x faster                                                      |
| regex_dna               | 160 ms                                                 | 150 ms: 1.07x faster                                                       |
| xml_etree_iterparse     | 72.6 ms                                                | 68.3 ms: 1.06x faster                                                      |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                      |
| pidigits                | 282 ms                                                 | 283 ms: 1.00x slower                                                       |
| unpickle                | 9.77 us                                                | 9.87 us: 1.01x slower                                                      |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                                      |
| gc_traversal            | 2.40 ms                                                | 2.43 ms: 1.01x slower                                                      |
| unpickle_list           | 2.66 us                                                | 2.71 us: 1.02x slower                                                      |
| pickle                  | 7.36 us                                                | 7.55 us: 1.03x slower                                                      |
| bench_mp_pool           | 41.0 ms                                                | 42.5 ms: 1.04x slower                                                      |
| generators              | 32.9 ms                                                | 34.4 ms: 1.04x slower                                                      |
| regex_effbot            | 2.45 ms                                                | 2.61 ms: 1.07x slower                                                      |
| dask                    | 258 ms                                                 | 317 ms: 1.23x slower                                                       |
| coverage                | 40.8 ms                                                | 57.4 ms: 1.41x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                               |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

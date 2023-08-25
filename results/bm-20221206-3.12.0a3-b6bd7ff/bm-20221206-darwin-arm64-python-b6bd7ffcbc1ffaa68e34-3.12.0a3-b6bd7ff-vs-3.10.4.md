
# Results vs. 3.10.4

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: darwin-arm64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.17x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 168 ms: 1.21x faster                                                  |
| chameleon      | 5.84 ms                                                | 4.53 ms: 1.29x faster                                                 |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| html5lib       | 44.1 ms                                                | 36.4 ms: 1.21x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 65.3 ms: 1.44x faster                                                 |
| float          | 72.3 ms                                                | 57.9 ms: 1.25x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 77.2 ms: 1.25x faster                                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                 |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                                  |
| regex_effbot   | 2.45 ms                                                | 2.61 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.38 ms                                                | 6.12 ms: 1.37x faster                                                 |
| pickle_pure_python   | 284 us                                                 | 214 us: 1.33x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 161 us: 1.26x faster                                                  |
| xml_etree_process    | 45.1 ms                                                | 36.3 ms: 1.24x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 96.7 ms: 1.11x faster                                                 |
| xml_etree_generate   | 54.3 ms                                                | 50.4 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 69.6 ms: 1.04x faster                                                 |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| unpickle_list        | 2.66 us                                                | 2.57 us: 1.03x faster                                                 |
| unpickle             | 9.77 us                                                | 9.63 us: 1.01x faster                                                 |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle               | 7.36 us                                                | 7.60 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.3 ms: 1.02x faster                                                 |
| python_startup_no_site | 9.73 ms                                                | 10.2 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.24 ms: 1.45x faster                                                 |
| genshi_text     | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                 |
| django_template | 27.3 ms                                                | 21.9 ms: 1.25x faster                                                 |
| genshi_xml      | 37.6 ms                                                | 30.4 ms: 1.24x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 64.2 ns: 1.85x faster                                                 |
| deltablue               | 5.15 ms                                                | 2.85 ms: 1.80x faster                                                 |
| richards                | 51.4 ms                                                | 32.1 ms: 1.60x faster                                                 |
| scimark_lu              | 110 ms                                                 | 70.9 ms: 1.55x faster                                                 |
| raytrace                | 328 ms                                                 | 222 ms: 1.48x faster                                                  |
| async_tree_memoization  | 493 ms                                                 | 335 ms: 1.47x faster                                                  |
| mako                    | 10.5 ms                                                | 7.24 ms: 1.45x faster                                                 |
| nbody                   | 94.1 ms                                                | 65.3 ms: 1.44x faster                                                 |
| crypto_pyaes            | 78.0 ms                                                | 54.2 ms: 1.44x faster                                                 |
| go                      | 165 ms                                                 | 118 ms: 1.39x faster                                                  |
| json_dumps              | 8.38 ms                                                | 6.12 ms: 1.37x faster                                                 |
| async_tree_none         | 402 ms                                                 | 297 ms: 1.36x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 756 ms: 1.35x faster                                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.00 ms: 1.33x faster                                                 |
| pickle_pure_python      | 284 us                                                 | 214 us: 1.33x faster                                                  |
| thrift                  | 586 us                                                 | 447 us: 1.31x faster                                                  |
| pycparser               | 915 ms                                                 | 704 ms: 1.30x faster                                                  |
| chaos                   | 66.8 ms                                                | 51.5 ms: 1.30x faster                                                 |
| sqlglot_transpile       | 1.54 ms                                                | 1.19 ms: 1.30x faster                                                 |
| spectral_norm           | 96.4 ms                                                | 74.4 ms: 1.30x faster                                                 |
| chameleon               | 5.84 ms                                                | 4.53 ms: 1.29x faster                                                 |
| pyflate                 | 453 ms                                                 | 352 ms: 1.29x faster                                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 56.2 ms: 1.29x faster                                                 |
| logging_format          | 5.01 us                                                | 3.96 us: 1.26x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 161 us: 1.26x faster                                                  |
| create_gc_cycles        | 876 us                                                 | 694 us: 1.26x faster                                                  |
| hexiom                  | 6.32 ms                                                | 5.01 ms: 1.26x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.68 us: 1.26x faster                                                 |
| regex_compile           | 96.6 ms                                                | 77.2 ms: 1.25x faster                                                 |
| float                   | 72.3 ms                                                | 57.9 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.78 ms: 1.25x faster                                                 |
| genshi_text             | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                 |
| django_template         | 27.3 ms                                                | 21.9 ms: 1.25x faster                                                 |
| xml_etree_process       | 45.1 ms                                                | 36.3 ms: 1.24x faster                                                 |
| genshi_xml              | 37.6 ms                                                | 30.4 ms: 1.24x faster                                                 |
| scimark_sor             | 127 ms                                                 | 104 ms: 1.22x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 30.5 ms: 1.22x faster                                                 |
| pprint_safe_repr        | 609 ms                                                 | 502 ms: 1.21x faster                                                  |
| html5lib                | 44.1 ms                                                | 36.4 ms: 1.21x faster                                                 |
| 2to3                    | 202 ms                                                 | 168 ms: 1.21x faster                                                  |
| pprint_pformat          | 1.24 sec                                               | 1.03 sec: 1.21x faster                                                |
| async_tree_cpu_io_mixed | 670 ms                                                 | 556 ms: 1.20x faster                                                  |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| sqlglot_optimize        | 38.0 ms                                                | 32.1 ms: 1.18x faster                                                 |
| scimark_fft             | 232 ms                                                 | 198 ms: 1.17x faster                                                  |
| mypy2                   | 308 ms                                                 | 264 ms: 1.17x faster                                                  |
| fannkuch                | 317 ms                                                 | 273 ms: 1.16x faster                                                  |
| bench_thread_pool       | 548 us                                                 | 473 us: 1.16x faster                                                  |
| async_generators        | 233 ms                                                 | 207 ms: 1.13x faster                                                  |
| dask                    | 258 ms                                                 | 230 ms: 1.12x faster                                                  |
| regex_v8                | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                 |
| sqlglot_normalize       | 197 ms                                                 | 176 ms: 1.12x faster                                                  |
| sympy_integrate         | 13.4 ms                                                | 12.0 ms: 1.11x faster                                                 |
| deepcopy_memo           | 34.5 us                                                | 31.0 us: 1.11x faster                                                 |
| xml_etree_parse         | 107 ms                                                 | 96.7 ms: 1.11x faster                                                 |
| json                    | 3.10 ms                                                | 2.82 ms: 1.10x faster                                                 |
| sympy_expand            | 276 ms                                                 | 251 ms: 1.10x faster                                                  |
| deepcopy_reduce         | 2.38 us                                                | 2.17 us: 1.10x faster                                                 |
| deepcopy                | 278 us                                                 | 253 us: 1.10x faster                                                  |
| nqueens                 | 68.1 ms                                                | 62.2 ms: 1.10x faster                                                 |
| sympy_str               | 169 ms                                                 | 157 ms: 1.08x faster                                                  |
| telco                   | 3.68 ms                                                | 3.41 ms: 1.08x faster                                                 |
| xml_etree_generate      | 54.3 ms                                                | 50.4 ms: 1.08x faster                                                 |
| sympy_sum               | 94.3 ms                                                | 87.9 ms: 1.07x faster                                                 |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.40 us: 1.05x faster                                                 |
| xml_etree_iterparse     | 72.6 ms                                                | 69.6 ms: 1.04x faster                                                 |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| unpickle_list           | 2.66 us                                                | 2.57 us: 1.03x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                 |
| asyncio_tcp             | 673 ms                                                 | 653 ms: 1.03x faster                                                  |
| python_startup          | 12.6 ms                                                | 12.3 ms: 1.02x faster                                                 |
| coroutines              | 20.2 ms                                                | 19.9 ms: 1.02x faster                                                 |
| unpickle                | 9.77 us                                                | 9.63 us: 1.01x faster                                                 |
| mdp                     | 1.67 sec                                               | 1.66 sec: 1.01x faster                                                |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| gc_traversal            | 2.40 ms                                                | 2.41 ms: 1.01x slower                                                 |
| comprehensions          | 17.7 us                                                | 17.8 us: 1.01x slower                                                 |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| generators              | 32.9 ms                                                | 33.6 ms: 1.02x slower                                                 |
| pickle                  | 7.36 us                                                | 7.60 us: 1.03x slower                                                 |
| python_startup_no_site  | 9.73 ms                                                | 10.2 ms: 1.05x slower                                                 |
| regex_effbot            | 2.45 ms                                                | 2.61 ms: 1.07x slower                                                 |
| bench_mp_pool           | 41.0 ms                                                | 44.6 ms: 1.09x slower                                                 |
| unpack_sequence         | 38.7 ns                                                | 52.7 ns: 1.36x slower                                                 |
| coverage                | 40.8 ms                                                | 60.7 ms: 1.49x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (2): meteor_contest, pickle_list
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x


# Results vs. base

- fork: iritkatriel
- ref: InitializeHeader_noa
- machine: linux-x86_64
- commit hash: 94fa28c
- commit date: 2023-01-05
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.01x slower                                                        |
| chameleon      | 6.27 ms                                                                | 6.15 ms: 1.02x faster                                                       |
| docutils       | 2.49 sec                                                               | 2.51 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 72.0 ms                                                                | 73.0 ms: 1.01x slower                                                       |
| pidigits       | 193 ms                                                                 | 197 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 130 ms: 1.01x slower                                                        |
| regex_dna      | 208 ms                                                                 | 207 ms: 1.01x faster                                                        |
| regex_effbot   | 3.51 ms                                                                | 3.61 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.50 ms                                                                | 9.28 ms: 1.02x faster                                                       |
| json_loads           | 24.4 us                                                                | 23.7 us: 1.03x faster                                                       |
| pickle_dict          | 30.0 us                                                                | 31.0 us: 1.03x slower                                                       |
| pickle_list          | 3.98 us                                                                | 4.04 us: 1.02x slower                                                       |
| pickle_pure_python   | 283 us                                                                 | 287 us: 1.02x slower                                                        |
| unpickle             | 13.3 us                                                                | 12.9 us: 1.03x faster                                                       |
| unpickle_list        | 5.00 us                                                                | 4.96 us: 1.01x faster                                                       |
| unpickle_pure_python | 198 us                                                                 | 197 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 106 ms                                                                 | 102 ms: 1.04x faster                                                        |
| xml_etree_process    | 53.2 ms                                                                | 53.4 ms: 1.00x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (3): pickle, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.46 ms                                                                | 8.49 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.06 ms                                                                | 6.08 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 46.6 ms                                                                | 46.9 ms: 1.01x slower                                                       |
| mako           | 9.66 ms                                                                | 9.38 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3                    | 253 ms                                                                 | 254 ms: 1.01x slower                                                        |
| async_generators        | 351 ms                                                                 | 352 ms: 1.00x slower                                                        |
| async_tree_io           | 1.31 sec                                                               | 1.32 sec: 1.01x slower                                                      |
| async_tree_memoization  | 622 ms                                                                 | 647 ms: 1.04x slower                                                        |
| chameleon               | 6.27 ms                                                                | 6.15 ms: 1.02x faster                                                       |
| chaos                   | 69.5 ms                                                                | 67.4 ms: 1.03x faster                                                       |
| bench_thread_pool       | 777 us                                                                 | 779 us: 1.00x slower                                                        |
| coroutines              | 25.0 ms                                                                | 25.4 ms: 1.01x slower                                                       |
| coverage                | 102 ms                                                                 | 98.8 ms: 1.03x faster                                                       |
| crypto_pyaes            | 75.7 ms                                                                | 74.4 ms: 1.02x faster                                                       |
| deepcopy                | 329 us                                                                 | 330 us: 1.00x slower                                                        |
| deepcopy_reduce         | 2.91 us                                                                | 2.93 us: 1.01x slower                                                       |
| deltablue               | 3.22 ms                                                                | 3.29 ms: 1.02x slower                                                       |
| docutils                | 2.49 sec                                                               | 2.51 sec: 1.01x slower                                                      |
| dulwich_log             | 62.5 ms                                                                | 62.8 ms: 1.01x slower                                                       |
| fannkuch                | 372 ms                                                                 | 377 ms: 1.01x slower                                                        |
| float                   | 72.0 ms                                                                | 73.0 ms: 1.01x slower                                                       |
| generators              | 77.3 ms                                                                | 76.8 ms: 1.01x faster                                                       |
| genshi_xml              | 46.6 ms                                                                | 46.9 ms: 1.01x slower                                                       |
| go                      | 139 ms                                                                 | 135 ms: 1.03x faster                                                        |
| hexiom                  | 6.12 ms                                                                | 6.10 ms: 1.00x faster                                                       |
| json                    | 4.71 ms                                                                | 4.60 ms: 1.02x faster                                                       |
| json_dumps              | 9.50 ms                                                                | 9.28 ms: 1.02x faster                                                       |
| json_loads              | 24.4 us                                                                | 23.7 us: 1.03x faster                                                       |
| logging_format          | 6.32 us                                                                | 6.42 us: 1.02x slower                                                       |
| logging_silent          | 93.3 ns                                                                | 92.5 ns: 1.01x faster                                                       |
| logging_simple          | 5.74 us                                                                | 5.78 us: 1.01x slower                                                       |
| mako                    | 9.66 ms                                                                | 9.38 ms: 1.03x faster                                                       |
| mdp                     | 2.49 sec                                                               | 2.72 sec: 1.09x slower                                                      |
| nqueens                 | 81.0 ms                                                                | 77.8 ms: 1.04x faster                                                       |
| pathlib                 | 18.4 ms                                                                | 18.1 ms: 1.02x faster                                                       |
| pickle_dict             | 30.0 us                                                                | 31.0 us: 1.03x slower                                                       |
| pickle_list             | 3.98 us                                                                | 4.04 us: 1.02x slower                                                       |
| pickle_pure_python      | 283 us                                                                 | 287 us: 1.02x slower                                                        |
| pidigits                | 193 ms                                                                 | 197 ms: 1.02x slower                                                        |
| pprint_pformat          | 1.38 sec                                                               | 1.37 sec: 1.01x faster                                                      |
| pycparser               | 1.14 sec                                                               | 1.15 sec: 1.02x slower                                                      |
| pyflate                 | 399 ms                                                                 | 392 ms: 1.02x faster                                                        |
| python_startup          | 8.46 ms                                                                | 8.49 ms: 1.00x slower                                                       |
| python_startup_no_site  | 6.06 ms                                                                | 6.08 ms: 1.00x slower                                                       |
| raytrace                | 279 ms                                                                 | 287 ms: 1.03x slower                                                        |
| regex_compile           | 130 ms                                                                 | 130 ms: 1.01x slower                                                        |
| regex_dna               | 208 ms                                                                 | 207 ms: 1.01x faster                                                        |
| regex_effbot            | 3.51 ms                                                                | 3.61 ms: 1.03x slower                                                       |
| richards                | 41.4 ms                                                                | 42.3 ms: 1.02x slower                                                       |
| scimark_fft             | 309 ms                                                                 | 318 ms: 1.03x slower                                                        |
| scimark_lu              | 109 ms                                                                 | 110 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult | 4.30 ms                                                                | 4.36 ms: 1.01x slower                                                       |
| spectral_norm           | 95.1 ms                                                                | 97.1 ms: 1.02x slower                                                       |
| sqlglot_parse           | 1.39 ms                                                                | 1.41 ms: 1.02x slower                                                       |
| sqlglot_transpile       | 1.69 ms                                                                | 1.70 ms: 1.01x slower                                                       |
| sqlglot_optimize        | 50.7 ms                                                                | 50.9 ms: 1.00x slower                                                       |
| sqlglot_normalize       | 104 ms                                                                 | 104 ms: 1.01x faster                                                        |
| sqlite_synth            | 2.57 us                                                                | 2.60 us: 1.01x slower                                                       |
| sympy_expand            | 448 ms                                                                 | 457 ms: 1.02x slower                                                        |
| sympy_integrate         | 20.2 ms                                                                | 20.3 ms: 1.01x slower                                                       |
| sympy_sum               | 163 ms                                                                 | 164 ms: 1.01x slower                                                        |
| sympy_str               | 279 ms                                                                 | 282 ms: 1.01x slower                                                        |
| telco                   | 6.39 ms                                                                | 6.30 ms: 1.01x faster                                                       |
| thrift                  | 741 us                                                                 | 750 us: 1.01x slower                                                        |
| unpack_sequence         | 41.7 ns                                                                | 41.2 ns: 1.01x faster                                                       |
| unpickle                | 13.3 us                                                                | 12.9 us: 1.03x faster                                                       |
| unpickle_list           | 5.00 us                                                                | 4.96 us: 1.01x faster                                                       |
| unpickle_pure_python    | 198 us                                                                 | 197 us: 1.01x faster                                                        |
| xml_etree_iterparse     | 106 ms                                                                 | 102 ms: 1.04x faster                                                        |
| xml_etree_process       | 53.2 ms                                                                | 53.4 ms: 1.00x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (18): async_tree_none, async_tree_cpu_io_mixed, bench_mp_pool, deepcopy_memo, django_template, djangocms, genshi_text, html5lib, meteor_contest, mypy, nbody, pickle, pprint_safe_repr, regex_v8, scimark_monte_carlo, scimark_sor, xml_etree_parse, xml_etree_generate

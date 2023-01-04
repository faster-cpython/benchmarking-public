
# Results vs. base

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: d501577
- commit date: 2023-01-05
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 252 ms: 1.00x faster                                                    |
| chameleon      | 6.27 ms                                                                | 6.23 ms: 1.01x faster                                                   |
| docutils       | 2.49 sec                                                               | 2.49 sec: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 95.3 ms                                                                | 93.4 ms: 1.02x faster                                                   |
| pidigits       | 193 ms                                                                 | 198 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                 | 208 ms: 1.00x faster                                                    |
| regex_effbot   | 3.51 ms                                                                | 3.60 ms: 1.03x slower                                                   |
| regex_v8       | 22.5 ms                                                                | 22.5 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 9.50 ms                                                                | 9.36 ms: 1.01x faster                                                   |
| json_loads           | 24.4 us                                                                | 23.9 us: 1.02x faster                                                   |
| pickle_dict          | 30.0 us                                                                | 29.8 us: 1.00x faster                                                   |
| pickle_list          | 3.98 us                                                                | 4.00 us: 1.00x slower                                                   |
| unpickle             | 13.3 us                                                                | 13.0 us: 1.02x faster                                                   |
| unpickle_list        | 5.00 us                                                                | 4.94 us: 1.01x faster                                                   |
| unpickle_pure_python | 198 us                                                                 | 199 us: 1.00x slower                                                    |
| xml_etree_iterparse  | 106 ms                                                                 | 107 ms: 1.01x slower                                                    |
| xml_etree_generate   | 76.5 ms                                                                | 77.0 ms: 1.01x slower                                                   |
| xml_etree_process    | 53.2 ms                                                                | 53.7 ms: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (3): pickle, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.46 ms                                                                | 8.48 ms: 1.00x slower                                                   |
| python_startup_no_site | 6.06 ms                                                                | 6.07 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 32.5 ms                                                                | 32.7 ms: 1.00x slower                                                   |
| mako            | 9.66 ms                                                                | 9.71 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230105-linux-x86_64-python-f20c553a458659f247fa-3.12.0a3+-f20c553 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3                    | 253 ms                                                                 | 252 ms: 1.00x faster                                                    |
| async_tree_memoization  | 622 ms                                                                 | 638 ms: 1.03x slower                                                    |
| chameleon               | 6.27 ms                                                                | 6.23 ms: 1.01x faster                                                   |
| chaos                   | 69.5 ms                                                                | 67.5 ms: 1.03x faster                                                   |
| coverage                | 102 ms                                                                 | 100 ms: 1.02x faster                                                    |
| crypto_pyaes            | 75.7 ms                                                                | 74.3 ms: 1.02x faster                                                   |
| deepcopy                | 329 us                                                                 | 334 us: 1.02x slower                                                    |
| deepcopy_reduce         | 2.91 us                                                                | 2.97 us: 1.02x slower                                                   |
| deepcopy_memo           | 34.0 us                                                                | 34.4 us: 1.01x slower                                                   |
| django_template         | 32.5 ms                                                                | 32.7 ms: 1.00x slower                                                   |
| docutils                | 2.49 sec                                                               | 2.49 sec: 1.00x slower                                                  |
| dulwich_log             | 62.5 ms                                                                | 62.0 ms: 1.01x faster                                                   |
| fannkuch                | 372 ms                                                                 | 363 ms: 1.02x faster                                                    |
| generators              | 77.3 ms                                                                | 75.4 ms: 1.02x faster                                                   |
| go                      | 139 ms                                                                 | 134 ms: 1.03x faster                                                    |
| hexiom                  | 6.12 ms                                                                | 6.06 ms: 1.01x faster                                                   |
| json_dumps              | 9.50 ms                                                                | 9.36 ms: 1.01x faster                                                   |
| json_loads              | 24.4 us                                                                | 23.9 us: 1.02x faster                                                   |
| logging_format          | 6.32 us                                                                | 6.35 us: 1.01x slower                                                   |
| logging_silent          | 93.3 ns                                                                | 92.5 ns: 1.01x faster                                                   |
| mako                    | 9.66 ms                                                                | 9.71 ms: 1.01x slower                                                   |
| mdp                     | 2.49 sec                                                               | 2.74 sec: 1.10x slower                                                  |
| nbody                   | 95.3 ms                                                                | 93.4 ms: 1.02x faster                                                   |
| pathlib                 | 18.4 ms                                                                | 18.2 ms: 1.01x faster                                                   |
| pickle_dict             | 30.0 us                                                                | 29.8 us: 1.00x faster                                                   |
| pickle_list             | 3.98 us                                                                | 4.00 us: 1.00x slower                                                   |
| pidigits                | 193 ms                                                                 | 198 ms: 1.03x slower                                                    |
| pprint_safe_repr        | 669 ms                                                                 | 674 ms: 1.01x slower                                                    |
| pycparser               | 1.14 sec                                                               | 1.15 sec: 1.01x slower                                                  |
| python_startup          | 8.46 ms                                                                | 8.48 ms: 1.00x slower                                                   |
| python_startup_no_site  | 6.06 ms                                                                | 6.07 ms: 1.00x slower                                                   |
| raytrace                | 279 ms                                                                 | 284 ms: 1.02x slower                                                    |
| regex_dna               | 208 ms                                                                 | 208 ms: 1.00x faster                                                    |
| regex_effbot            | 3.51 ms                                                                | 3.60 ms: 1.03x slower                                                   |
| regex_v8                | 22.5 ms                                                                | 22.5 ms: 1.00x slower                                                   |
| scimark_sparse_mat_mult | 4.30 ms                                                                | 3.98 ms: 1.08x faster                                                   |
| spectral_norm           | 95.1 ms                                                                | 95.9 ms: 1.01x slower                                                   |
| sqlglot_parse           | 1.39 ms                                                                | 1.40 ms: 1.01x slower                                                   |
| sqlglot_optimize        | 50.7 ms                                                                | 51.0 ms: 1.00x slower                                                   |
| sqlglot_normalize       | 104 ms                                                                 | 106 ms: 1.02x slower                                                    |
| sqlite_synth            | 2.57 us                                                                | 2.59 us: 1.01x slower                                                   |
| sympy_expand            | 448 ms                                                                 | 455 ms: 1.01x slower                                                    |
| sympy_integrate         | 20.2 ms                                                                | 20.3 ms: 1.01x slower                                                   |
| sympy_str               | 279 ms                                                                 | 281 ms: 1.01x slower                                                    |
| unpack_sequence         | 41.7 ns                                                                | 42.5 ns: 1.02x slower                                                   |
| unpickle                | 13.3 us                                                                | 13.0 us: 1.02x faster                                                   |
| unpickle_list           | 5.00 us                                                                | 4.94 us: 1.01x faster                                                   |
| unpickle_pure_python    | 198 us                                                                 | 199 us: 1.00x slower                                                    |
| xml_etree_iterparse     | 106 ms                                                                 | 107 ms: 1.01x slower                                                    |
| xml_etree_generate      | 76.5 ms                                                                | 77.0 ms: 1.01x slower                                                   |
| xml_etree_process       | 53.2 ms                                                                | 53.7 ms: 1.01x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (33): async_generators, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, bench_mp_pool, bench_thread_pool, coroutines, deltablue, djangocms, float, genshi_text, genshi_xml, html5lib, json, logging_simple, meteor_contest, mypy, nqueens, pickle, pickle_pure_python, pprint_pformat, pyflate, regex_compile, richards, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, sqlglot_transpile, sympy_sum, telco, thrift, xml_etree_parse

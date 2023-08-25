
# Results vs. base

- fork: eduardo-elizondo
- ref: immortal_references
- machine: darwin-arm64
- commit hash: 1dfe27a
- commit date: 2023-01-08
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 163 ms                                                                 | 178 ms: 1.10x slower                                                              |
| html5lib       | 35.0 ms                                                                | 33.6 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): chameleon, docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 51.8 ms                                                                | 52.0 ms: 1.00x slower                                                             |
| pidigits       | 281 ms                                                                 | 282 ms: 1.01x slower                                                              |
| nbody          | 63.7 ms                                                                | 66.3 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 74.6 ms                                                                | 69.8 ms: 1.07x faster                                                             |
| regex_effbot   | 2.63 ms                                                                | 2.63 ms: 1.00x faster                                                             |
| regex_dna      | 149 ms                                                                 | 149 ms: 1.00x slower                                                              |
| regex_v8       | 15.7 ms                                                                | 16.1 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 69.9 ms                                                                | 66.3 ms: 1.05x faster                                                             |
| xml_etree_parse      | 99.2 ms                                                                | 94.7 ms: 1.05x faster                                                             |
| pickle_pure_python   | 194 us                                                                 | 187 us: 1.04x faster                                                              |
| json_dumps           | 6.11 ms                                                                | 5.95 ms: 1.03x faster                                                             |
| unpickle_list        | 2.72 us                                                                | 2.66 us: 1.02x faster                                                             |
| pickle_list          | 2.88 us                                                                | 2.86 us: 1.01x faster                                                             |
| unpickle_pure_python | 143 us                                                                 | 143 us: 1.01x faster                                                              |
| json_loads           | 16.2 us                                                                | 16.3 us: 1.01x slower                                                             |
| pickle_dict          | 17.9 us                                                                | 18.1 us: 1.01x slower                                                             |
| pickle               | 7.53 us                                                                | 7.69 us: 1.02x slower                                                             |
| xml_etree_generate   | 48.3 ms                                                                | 49.3 ms: 1.02x slower                                                             |
| unpickle             | 9.55 us                                                                | 10.2 us: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 10.4 ms                                                                | 7.31 ms: 1.42x faster                                                             |
| python_startup         | 12.4 ms                                                                | 9.33 ms: 1.33x faster                                                             |
| Geometric mean         | (ref)                                                                  | 1.37x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 15.1 ms                                                                | 14.4 ms: 1.05x faster                                                             |
| django_template | 21.7 ms                                                                | 20.9 ms: 1.04x faster                                                             |
| mako            | 8.14 ms                                                                | 8.51 ms: 1.05x slower                                                             |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 | bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site  | 10.4 ms                                                                | 7.31 ms: 1.42x faster                                                             |
| pathlib                 | 28.0 ms                                                                | 20.8 ms: 1.35x faster                                                             |
| python_startup          | 12.4 ms                                                                | 9.33 ms: 1.33x faster                                                             |
| unpack_sequence         | 32.7 ns                                                                | 28.8 ns: 1.14x faster                                                             |
| hexiom                  | 4.95 ms                                                                | 4.44 ms: 1.11x faster                                                             |
| coroutines              | 18.7 ms                                                                | 16.8 ms: 1.11x faster                                                             |
| chaos                   | 50.4 ms                                                                | 46.1 ms: 1.09x faster                                                             |
| fannkuch                | 254 ms                                                                 | 232 ms: 1.09x faster                                                              |
| nqueens                 | 61.0 ms                                                                | 55.9 ms: 1.09x faster                                                             |
| asyncio_tcp             | 445 ms                                                                 | 412 ms: 1.08x faster                                                              |
| scimark_monte_carlo     | 49.6 ms                                                                | 46.2 ms: 1.07x faster                                                             |
| regex_compile           | 74.6 ms                                                                | 69.8 ms: 1.07x faster                                                             |
| richards                | 30.7 ms                                                                | 28.9 ms: 1.06x faster                                                             |
| dulwich_log             | 29.6 ms                                                                | 27.9 ms: 1.06x faster                                                             |
| go                      | 109 ms                                                                 | 103 ms: 1.06x faster                                                              |
| xml_etree_iterparse     | 69.9 ms                                                                | 66.3 ms: 1.05x faster                                                             |
| sympy_str               | 152 ms                                                                 | 145 ms: 1.05x faster                                                              |
| xml_etree_parse         | 99.2 ms                                                                | 94.7 ms: 1.05x faster                                                             |
| genshi_text             | 15.1 ms                                                                | 14.4 ms: 1.05x faster                                                             |
| logging_silent          | 66.7 ns                                                                | 63.7 ns: 1.05x faster                                                             |
| async_tree_memoization  | 332 ms                                                                 | 317 ms: 1.05x faster                                                              |
| bench_thread_pool       | 463 us                                                                 | 443 us: 1.04x faster                                                              |
| async_tree_none         | 288 ms                                                                 | 276 ms: 1.04x faster                                                              |
| logging_simple          | 3.44 us                                                                | 3.30 us: 1.04x faster                                                             |
| deepcopy_reduce         | 1.93 us                                                                | 1.85 us: 1.04x faster                                                             |
| sympy_expand            | 242 ms                                                                 | 232 ms: 1.04x faster                                                              |
| html5lib                | 35.0 ms                                                                | 33.6 ms: 1.04x faster                                                             |
| sqlglot_parse           | 1.03 ms                                                                | 991 us: 1.04x faster                                                              |
| async_tree_io           | 749 ms                                                                 | 720 ms: 1.04x faster                                                              |
| pickle_pure_python      | 194 us                                                                 | 187 us: 1.04x faster                                                              |
| logging_format          | 3.73 us                                                                | 3.59 us: 1.04x faster                                                             |
| sympy_sum               | 86.4 ms                                                                | 83.2 ms: 1.04x faster                                                             |
| deltablue               | 2.65 ms                                                                | 2.56 ms: 1.04x faster                                                             |
| django_template         | 21.7 ms                                                                | 20.9 ms: 1.04x faster                                                             |
| sqlglot_transpile       | 1.19 ms                                                                | 1.15 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed | 547 ms                                                                 | 530 ms: 1.03x faster                                                              |
| deepcopy                | 221 us                                                                 | 215 us: 1.03x faster                                                              |
| bench_mp_pool           | 44.1 ms                                                                | 42.9 ms: 1.03x faster                                                             |
| pprint_pformat          | 936 ms                                                                 | 910 ms: 1.03x faster                                                              |
| json_dumps              | 6.11 ms                                                                | 5.95 ms: 1.03x faster                                                             |
| pprint_safe_repr        | 460 ms                                                                 | 448 ms: 1.03x faster                                                              |
| deepcopy_memo           | 26.2 us                                                                | 25.6 us: 1.02x faster                                                             |
| async_generators        | 201 ms                                                                 | 197 ms: 1.02x faster                                                              |
| unpickle_list           | 2.72 us                                                                | 2.66 us: 1.02x faster                                                             |
| thrift                  | 440 us                                                                 | 431 us: 1.02x faster                                                              |
| create_gc_cycles        | 690 us                                                                 | 677 us: 1.02x faster                                                              |
| coverage                | 57.2 ms                                                                | 56.2 ms: 1.02x faster                                                             |
| sympy_integrate         | 11.4 ms                                                                | 11.2 ms: 1.02x faster                                                             |
| pycparser               | 677 ms                                                                 | 667 ms: 1.02x faster                                                              |
| crypto_pyaes            | 52.8 ms                                                                | 52.0 ms: 1.01x faster                                                             |
| sqlglot_normalize       | 172 ms                                                                 | 170 ms: 1.01x faster                                                              |
| telco                   | 3.49 ms                                                                | 3.45 ms: 1.01x faster                                                             |
| spectral_norm           | 73.7 ms                                                                | 73.0 ms: 1.01x faster                                                             |
| sqlglot_optimize        | 31.4 ms                                                                | 31.1 ms: 1.01x faster                                                             |
| meteor_contest          | 75.0 ms                                                                | 74.3 ms: 1.01x faster                                                             |
| mdp                     | 1.51 sec                                                               | 1.50 sec: 1.01x faster                                                            |
| generators              | 33.9 ms                                                                | 33.7 ms: 1.01x faster                                                             |
| pickle_list             | 2.88 us                                                                | 2.86 us: 1.01x faster                                                             |
| gc_traversal            | 2.42 ms                                                                | 2.40 ms: 1.01x faster                                                             |
| unpickle_pure_python    | 143 us                                                                 | 143 us: 1.01x faster                                                              |
| regex_effbot            | 2.63 ms                                                                | 2.63 ms: 1.00x faster                                                             |
| regex_dna               | 149 ms                                                                 | 149 ms: 1.00x slower                                                              |
| pyflate                 | 319 ms                                                                 | 319 ms: 1.00x slower                                                              |
| float                   | 51.8 ms                                                                | 52.0 ms: 1.00x slower                                                             |
| pidigits                | 281 ms                                                                 | 282 ms: 1.01x slower                                                              |
| json_loads              | 16.2 us                                                                | 16.3 us: 1.01x slower                                                             |
| pickle_dict             | 17.9 us                                                                | 18.1 us: 1.01x slower                                                             |
| raytrace                | 220 ms                                                                 | 222 ms: 1.01x slower                                                              |
| json                    | 2.79 ms                                                                | 2.83 ms: 1.01x slower                                                             |
| scimark_fft             | 195 ms                                                                 | 199 ms: 1.02x slower                                                              |
| pickle                  | 7.53 us                                                                | 7.69 us: 1.02x slower                                                             |
| xml_etree_generate      | 48.3 ms                                                                | 49.3 ms: 1.02x slower                                                             |
| scimark_sparse_mat_mult | 2.83 ms                                                                | 2.90 ms: 1.02x slower                                                             |
| regex_v8                | 15.7 ms                                                                | 16.1 ms: 1.02x slower                                                             |
| nbody                   | 63.7 ms                                                                | 66.3 ms: 1.04x slower                                                             |
| scimark_lu              | 72.7 ms                                                                | 75.7 ms: 1.04x slower                                                             |
| sqlite_synth            | 1.34 us                                                                | 1.40 us: 1.04x slower                                                             |
| mako                    | 8.14 ms                                                                | 8.51 ms: 1.05x slower                                                             |
| unpickle                | 9.55 us                                                                | 10.2 us: 1.07x slower                                                             |
| scimark_sor             | 78.8 ms                                                                | 84.0 ms: 1.07x slower                                                             |
| 2to3                    | 163 ms                                                                 | 178 ms: 1.10x slower                                                              |
| dask                    | 225 ms                                                                 | 315 ms: 1.40x slower                                                              |
| Geometric mean          | (ref)                                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (4): xml_etree_process, genshi_xml, chameleon, docutils
Ignored benchmarks (2) of results/bm-20230108-3.12.0a3+-e47b139/bm-20230108-darwin-arm64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139.json: comprehensions, mypy2
Ignored benchmarks (1) of results/bm-20230108-3.12.0a3+-1dfe27a/bm-20230108-darwin-arm64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

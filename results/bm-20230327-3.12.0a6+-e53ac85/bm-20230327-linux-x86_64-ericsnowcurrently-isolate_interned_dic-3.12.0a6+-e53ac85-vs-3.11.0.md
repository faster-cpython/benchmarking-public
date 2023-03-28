
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: e53ac85
- commit date: 2023-03-27
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 253 ms: 1.02x faster                                                              |
| chameleon      | 6.52 ms                                                             | 6.43 ms: 1.01x faster                                                             |
| docutils       | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                            |
| html5lib       | 64.0 ms                                                             | 62.2 ms: 1.03x faster                                                             |
| tornado_http   | 96.7 ms                                                             | 91.5 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                               | 1.03x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.1 ms: 1.11x faster                                                             |
| pidigits       | 197 ms                                                              | 188 ms: 1.05x faster                                                              |
| float          | 76.0 ms                                                             | 73.8 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                               | 1.06x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                              | 134 ms: 1.02x faster                                                              |
| regex_v8       | 22.0 ms                                                             | 21.7 ms: 1.01x faster                                                             |
| regex_dna      | 196 ms                                                              | 205 ms: 1.04x slower                                                              |
| regex_effbot   | 3.32 ms                                                             | 3.73 ms: 1.12x slower                                                             |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.53 ms: 1.32x faster                                                             |
| unpickle_pure_python | 228 us                                                              | 203 us: 1.13x faster                                                              |
| xml_etree_parse      | 162 ms                                                              | 148 ms: 1.10x faster                                                              |
| xml_etree_iterparse  | 108 ms                                                              | 98.5 ms: 1.09x faster                                                             |
| json_loads           | 26.2 us                                                             | 24.3 us: 1.08x faster                                                             |
| pickle_pure_python   | 307 us                                                              | 285 us: 1.08x faster                                                              |
| unpickle_list        | 4.96 us                                                             | 4.99 us: 1.01x slower                                                             |
| pickle_dict          | 30.9 us                                                             | 31.1 us: 1.01x slower                                                             |
| unpickle             | 13.2 us                                                             | 13.5 us: 1.02x slower                                                             |
| xml_etree_process    | 54.1 ms                                                             | 55.4 ms: 1.02x slower                                                             |
| pickle_list          | 4.03 us                                                             | 4.13 us: 1.03x slower                                                             |
| xml_etree_generate   | 76.5 ms                                                             | 80.2 ms: 1.05x slower                                                             |
| pickle               | 9.79 us                                                             | 10.3 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.04x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.85 ms: 1.04x slower                                                             |
| python_startup_no_site | 5.98 ms                                                             | 6.54 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 47.1 ms: 1.10x faster                                                             |
| genshi_text     | 21.8 ms                                                             | 21.0 ms: 1.04x faster                                                             |
| mako            | 9.82 ms                                                             | 9.99 ms: 1.02x slower                                                             |
| django_template | 32.9 ms                                                             | 33.7 ms: 1.02x slower                                                             |
| Geometric mean  | (ref)                                                               | 1.02x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 28.7 ms: 2.56x faster                                                             |
| asyncio_tcp             | 888 ms                                                              | 506 ms: 1.75x faster                                                              |
| json_dumps              | 12.5 ms                                                             | 9.53 ms: 1.32x faster                                                             |
| mypy2                   | 422 ms                                                              | 333 ms: 1.27x faster                                                              |
| unpack_sequence         | 49.5 ns                                                             | 42.0 ns: 1.18x faster                                                             |
| deltablue               | 3.66 ms                                                             | 3.23 ms: 1.13x faster                                                             |
| unpickle_pure_python    | 228 us                                                              | 203 us: 1.13x faster                                                              |
| coroutines              | 26.3 ms                                                             | 23.4 ms: 1.12x faster                                                             |
| nbody                   | 96.7 ms                                                             | 87.1 ms: 1.11x faster                                                             |
| genshi_xml              | 51.8 ms                                                             | 47.1 ms: 1.10x faster                                                             |
| xml_etree_parse         | 162 ms                                                              | 148 ms: 1.10x faster                                                              |
| xml_etree_iterparse     | 108 ms                                                              | 98.5 ms: 1.09x faster                                                             |
| scimark_fft             | 328 ms                                                              | 303 ms: 1.08x faster                                                              |
| json_loads              | 26.2 us                                                             | 24.3 us: 1.08x faster                                                             |
| pickle_pure_python      | 307 us                                                              | 285 us: 1.08x faster                                                              |
| spectral_norm           | 99.5 ms                                                             | 93.1 ms: 1.07x faster                                                             |
| hexiom                  | 6.48 ms                                                             | 6.08 ms: 1.07x faster                                                             |
| tornado_http            | 96.7 ms                                                             | 91.5 ms: 1.06x faster                                                             |
| logging_simple          | 6.09 us                                                             | 5.77 us: 1.06x faster                                                             |
| mdp                     | 2.64 sec                                                            | 2.50 sec: 1.05x faster                                                            |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.24 ms: 1.05x faster                                                             |
| nqueens                 | 84.0 ms                                                             | 79.8 ms: 1.05x faster                                                             |
| logging_format          | 6.64 us                                                             | 6.31 us: 1.05x faster                                                             |
| deepcopy_memo           | 36.4 us                                                             | 34.6 us: 1.05x faster                                                             |
| pidigits                | 197 ms                                                              | 188 ms: 1.05x faster                                                              |
| json                    | 4.86 ms                                                             | 4.65 ms: 1.05x faster                                                             |
| raytrace                | 292 ms                                                              | 280 ms: 1.04x faster                                                              |
| aiohttp                 | 1.05 ms                                                             | 1.01 ms: 1.04x faster                                                             |
| coverage                | 101 ms                                                              | 97.3 ms: 1.04x faster                                                             |
| genshi_text             | 21.8 ms                                                             | 21.0 ms: 1.04x faster                                                             |
| richards                | 45.7 ms                                                             | 44.0 ms: 1.04x faster                                                             |
| logging_silent          | 98.7 ns                                                             | 95.2 ns: 1.04x faster                                                             |
| sqlglot_optimize        | 53.4 ms                                                             | 51.5 ms: 1.04x faster                                                             |
| sympy_expand            | 477 ms                                                              | 461 ms: 1.03x faster                                                              |
| deepcopy                | 339 us                                                              | 328 us: 1.03x faster                                                              |
| meteor_contest          | 106 ms                                                              | 103 ms: 1.03x faster                                                              |
| bench_thread_pool       | 820 us                                                              | 793 us: 1.03x faster                                                              |
| sympy_integrate         | 21.0 ms                                                             | 20.4 ms: 1.03x faster                                                             |
| sympy_str               | 291 ms                                                              | 283 ms: 1.03x faster                                                              |
| gunicorn                | 1.13 ms                                                             | 1.10 ms: 1.03x faster                                                             |
| float                   | 76.0 ms                                                             | 73.8 ms: 1.03x faster                                                             |
| html5lib                | 64.0 ms                                                             | 62.2 ms: 1.03x faster                                                             |
| pycparser               | 1.14 sec                                                            | 1.11 sec: 1.03x faster                                                            |
| gc_traversal            | 3.63 ms                                                             | 3.53 ms: 1.03x faster                                                             |
| docutils                | 2.59 sec                                                            | 2.53 sec: 1.02x faster                                                            |
| fannkuch                | 384 ms                                                              | 375 ms: 1.02x faster                                                              |
| sqlglot_normalize       | 108 ms                                                              | 106 ms: 1.02x faster                                                              |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.3 ms: 1.02x faster                                                             |
| pprint_pformat          | 1.45 sec                                                            | 1.42 sec: 1.02x faster                                                            |
| 2to3                    | 257 ms                                                              | 253 ms: 1.02x faster                                                              |
| sqlalchemy_declarative  | 138 ms                                                              | 136 ms: 1.02x faster                                                              |
| sqlalchemy_imperative   | 18.0 ms                                                             | 17.7 ms: 1.02x faster                                                             |
| regex_compile           | 137 ms                                                              | 134 ms: 1.02x faster                                                              |
| deepcopy_reduce         | 2.96 us                                                             | 2.91 us: 1.02x faster                                                             |
| chameleon               | 6.52 ms                                                             | 6.43 ms: 1.01x faster                                                             |
| regex_v8                | 22.0 ms                                                             | 21.7 ms: 1.01x faster                                                             |
| pprint_safe_repr        | 701 ms                                                              | 693 ms: 1.01x faster                                                              |
| scimark_sor             | 115 ms                                                              | 113 ms: 1.01x faster                                                              |
| pathlib                 | 18.2 ms                                                             | 18.1 ms: 1.01x faster                                                             |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                                              |
| chaos                   | 68.0 ms                                                             | 67.4 ms: 1.01x faster                                                             |
| create_gc_cycles        | 1.48 ms                                                             | 1.47 ms: 1.01x faster                                                             |
| dulwich_log             | 63.6 ms                                                             | 64.0 ms: 1.01x slower                                                             |
| unpickle_list           | 4.96 us                                                             | 4.99 us: 1.01x slower                                                             |
| pickle_dict             | 30.9 us                                                             | 31.1 us: 1.01x slower                                                             |
| go                      | 138 ms                                                              | 140 ms: 1.01x slower                                                              |
| crypto_pyaes            | 73.8 ms                                                             | 74.5 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                              | 745 ms: 1.01x slower                                                              |
| async_tree_io           | 1.28 sec                                                            | 1.30 sec: 1.02x slower                                                            |
| pyflate                 | 414 ms                                                              | 420 ms: 1.02x slower                                                              |
| mako                    | 9.82 ms                                                             | 9.99 ms: 1.02x slower                                                             |
| thrift                  | 766 us                                                              | 779 us: 1.02x slower                                                              |
| unpickle                | 13.2 us                                                             | 13.5 us: 1.02x slower                                                             |
| xml_etree_process       | 54.1 ms                                                             | 55.4 ms: 1.02x slower                                                             |
| django_template         | 32.9 ms                                                             | 33.7 ms: 1.02x slower                                                             |
| pickle_list             | 4.03 us                                                             | 4.13 us: 1.03x slower                                                             |
| sqlglot_transpile       | 1.65 ms                                                             | 1.71 ms: 1.04x slower                                                             |
| sqlite_synth            | 2.51 us                                                             | 2.61 us: 1.04x slower                                                             |
| regex_dna               | 196 ms                                                              | 205 ms: 1.04x slower                                                              |
| python_startup          | 8.49 ms                                                             | 8.85 ms: 1.04x slower                                                             |
| sqlglot_parse           | 1.36 ms                                                             | 1.42 ms: 1.04x slower                                                             |
| xml_etree_generate      | 76.5 ms                                                             | 80.2 ms: 1.05x slower                                                             |
| pickle                  | 9.79 us                                                             | 10.3 us: 1.05x slower                                                             |
| async_tree_memoization  | 621 ms                                                              | 656 ms: 1.06x slower                                                              |
| comprehensions          | 22.2 us                                                             | 23.8 us: 1.07x slower                                                             |
| python_startup_no_site  | 5.98 ms                                                             | 6.54 ms: 1.09x slower                                                             |
| regex_effbot            | 3.32 ms                                                             | 3.73 ms: 1.12x slower                                                             |
| async_generators        | 361 ms                                                              | 413 ms: 1.14x slower                                                              |
| dask                    | 368 ms                                                              | 509 ms: 1.38x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.04x faster                                                                      |

Benchmark hidden because not significant (5): telco, bench_mp_pool, djangocms, scimark_lu, async_tree_none
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: flaskblogging, pylint

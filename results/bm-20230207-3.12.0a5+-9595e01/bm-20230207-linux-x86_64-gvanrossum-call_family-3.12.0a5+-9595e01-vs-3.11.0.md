
# Results vs. 3.11.0

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: 9595e01
- commit date: 2023-02-07
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                              |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                            |
| html5lib       | 64.8 ms                                                | 61.1 ms: 1.06x faster                                             |
| tornado_http   | 96.5 ms                                                | 93.7 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.7 ms: 1.04x faster                                             |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                              |
| nbody          | 90.0 ms                                                | 96.0 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                              |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.03x faster                                             |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                              |
| regex_effbot   | 3.46 ms                                                | 3.62 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.53 ms: 1.30x faster                                             |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                              |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                              |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                              |
| json_loads           | 26.1 us                                                | 24.3 us: 1.07x faster                                             |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| xml_etree_process    | 53.7 ms                                                | 53.2 ms: 1.01x faster                                             |
| pickle_dict          | 31.2 us                                                | 31.6 us: 1.01x slower                                             |
| xml_etree_generate   | 75.9 ms                                                | 77.4 ms: 1.02x slower                                             |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (3): pickle_list, unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.91 ms: 1.04x slower                                             |
| python_startup_no_site | 6.04 ms                                                | 6.47 ms: 1.07x slower                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.5 ms: 1.10x faster                                             |
| genshi_text     | 21.5 ms                                                | 20.7 ms: 1.04x faster                                             |
| mako            | 9.83 ms                                                | 9.92 ms: 1.01x slower                                             |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                             |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 492 ms: 1.80x faster                                              |
| json_dumps              | 12.4 ms                                                | 9.53 ms: 1.30x faster                                             |
| mypy2                   | 420 ms                                                 | 330 ms: 1.27x faster                                              |
| deltablue               | 3.66 ms                                                | 3.16 ms: 1.16x faster                                             |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                              |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.04 ms: 1.14x faster                                             |
| genshi_xml              | 51.4 ms                                                | 46.5 ms: 1.10x faster                                             |
| richards                | 46.1 ms                                                | 42.2 ms: 1.09x faster                                             |
| fannkuch                | 384 ms                                                 | 355 ms: 1.08x faster                                              |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                              |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                              |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                              |
| json_loads              | 26.1 us                                                | 24.3 us: 1.07x faster                                             |
| unpack_sequence         | 44.5 ns                                                | 41.6 ns: 1.07x faster                                             |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                              |
| coroutines              | 26.2 ms                                                | 24.5 ms: 1.07x faster                                             |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.07x faster                                              |
| hexiom                  | 6.34 ms                                                | 5.96 ms: 1.06x faster                                             |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.06x faster                                              |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                             |
| html5lib                | 64.8 ms                                                | 61.1 ms: 1.06x faster                                             |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                              |
| scimark_fft             | 325 ms                                                 | 309 ms: 1.05x faster                                              |
| logging_silent          | 98.0 ns                                                | 93.3 ns: 1.05x faster                                             |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                             |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                              |
| bench_thread_pool       | 817 us                                                 | 781 us: 1.04x faster                                              |
| crypto_pyaes            | 75.7 ms                                                | 72.6 ms: 1.04x faster                                             |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                            |
| float                   | 76.8 ms                                                | 73.7 ms: 1.04x faster                                             |
| genshi_text             | 21.5 ms                                                | 20.7 ms: 1.04x faster                                             |
| coverage                | 99.3 ms                                                | 95.6 ms: 1.04x faster                                             |
| chaos                   | 68.7 ms                                                | 66.1 ms: 1.04x faster                                             |
| pyflate                 | 419 ms                                                 | 404 ms: 1.04x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                            |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                             |
| json                    | 4.87 ms                                                | 4.70 ms: 1.03x faster                                             |
| nqueens                 | 83.8 ms                                                | 81.0 ms: 1.03x faster                                             |
| thrift                  | 760 us                                                 | 735 us: 1.03x faster                                              |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                              |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                              |
| tornado_http            | 96.5 ms                                                | 93.7 ms: 1.03x faster                                             |
| spectral_norm           | 98.1 ms                                                | 95.4 ms: 1.03x faster                                             |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                            |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.03x faster                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 66.2 ms: 1.03x faster                                             |
| async_generators        | 356 ms                                                 | 347 ms: 1.03x faster                                              |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.03x faster                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.03x faster                                             |
| pprint_safe_repr        | 706 ms                                                 | 689 ms: 1.02x faster                                              |
| deepcopy_memo           | 35.8 us                                                | 35.0 us: 1.02x faster                                             |
| logging_simple          | 6.02 us                                                | 5.89 us: 1.02x faster                                             |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                              |
| deepcopy                | 341 us                                                 | 336 us: 1.02x faster                                              |
| dulwich_log             | 64.0 ms                                                | 63.0 ms: 1.02x faster                                             |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                              |
| mdp                     | 2.63 sec                                               | 2.59 sec: 1.01x faster                                            |
| deepcopy_reduce         | 3.02 us                                                | 2.98 us: 1.01x faster                                             |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| xml_etree_process       | 53.7 ms                                                | 53.2 ms: 1.01x faster                                             |
| pathlib                 | 18.1 ms                                                | 18.0 ms: 1.01x faster                                             |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                              |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                              |
| mako                    | 9.83 ms                                                | 9.92 ms: 1.01x slower                                             |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                            |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                             |
| pickle_dict             | 31.2 us                                                | 31.6 us: 1.01x slower                                             |
| xml_etree_generate      | 75.9 ms                                                | 77.4 ms: 1.02x slower                                             |
| gc_traversal            | 3.82 ms                                                | 3.91 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed | 736 ms                                                 | 757 ms: 1.03x slower                                              |
| generators              | 73.5 ms                                                | 75.7 ms: 1.03x slower                                             |
| meteor_contest          | 104 ms                                                 | 108 ms: 1.03x slower                                              |
| async_tree_memoization  | 624 ms                                                 | 647 ms: 1.04x slower                                              |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                             |
| python_startup          | 8.58 ms                                                | 8.91 ms: 1.04x slower                                             |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                             |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                             |
| regex_effbot            | 3.46 ms                                                | 3.62 ms: 1.05x slower                                             |
| nbody                   | 90.0 ms                                                | 96.0 ms: 1.07x slower                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.47 ms: 1.07x slower                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (11): djangocms, sqlalchemy_imperative, async_tree_none, chameleon, sqlalchemy_declarative, pickle_list, bench_mp_pool, unpickle, logging_format, telco, unpickle_list
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint

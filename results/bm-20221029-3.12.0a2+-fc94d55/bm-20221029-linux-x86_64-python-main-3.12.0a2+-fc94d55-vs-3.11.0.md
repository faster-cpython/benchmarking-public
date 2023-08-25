
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: fc94d55
- commit date: 2022-10-29
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.37 ms: 1.02x faster                                  |
| html5lib       | 64.5 ms                                                | 59.5 ms: 1.08x faster                                  |
| tornado_http   | 96.3 ms                                                | 93.1 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.9 ms: 1.06x faster                                  |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| nbody          | 93.1 ms                                                | 98.1 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.69 ms: 1.08x faster                                  |
| regex_compile  | 138 ms                                                 | 130 ms: 1.07x faster                                   |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                   |
| regex_v8       | 22.0 ms                                                | 22.9 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.31 ms: 1.35x faster                                  |
| json_loads           | 26.5 us                                                | 23.5 us: 1.13x faster                                  |
| unpickle_pure_python | 228 us                                                 | 205 us: 1.11x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                   |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                   |
| unpickle             | 13.7 us                                                | 12.9 us: 1.06x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 53.1 ms: 1.01x faster                                  |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                  |
| pickle_list          | 4.11 us                                                | 4.16 us: 1.01x slower                                  |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.02x slower                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.37 ms: 1.02x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.08 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 49.2 ms: 1.05x faster                                  |
| mako            | 10.1 ms                                                | 9.72 ms: 1.04x faster                                  |
| genshi_text     | 21.6 ms                                                | 21.1 ms: 1.02x faster                                  |
| django_template | 32.6 ms                                                | 32.0 ms: 1.02x faster                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.31 ms: 1.35x faster                                  |
| json_loads              | 26.5 us                                                | 23.5 us: 1.13x faster                                  |
| deltablue               | 3.67 ms                                                | 3.30 ms: 1.11x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 205 us: 1.11x faster                                   |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                   |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                  |
| html5lib                | 64.5 ms                                                | 59.5 ms: 1.08x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.69 ms: 1.08x faster                                  |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                 |
| deepcopy_memo           | 37.0 us                                                | 34.3 us: 1.08x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                   |
| logging_silent          | 101 ns                                                 | 94.4 ns: 1.07x faster                                  |
| regex_compile           | 138 ms                                                 | 130 ms: 1.07x faster                                   |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                 |
| spectral_norm           | 100 ms                                                 | 94.1 ms: 1.06x faster                                  |
| float                   | 77.2 ms                                                | 72.9 ms: 1.06x faster                                  |
| json                    | 4.94 ms                                                | 4.67 ms: 1.06x faster                                  |
| unpickle                | 13.7 us                                                | 12.9 us: 1.06x faster                                  |
| richards                | 45.7 ms                                                | 43.4 ms: 1.05x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.27 ms: 1.05x faster                                  |
| genshi_xml              | 51.8 ms                                                | 49.2 ms: 1.05x faster                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.05x faster                                  |
| pyflate                 | 418 ms                                                 | 399 ms: 1.05x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                   |
| coroutines              | 25.5 ms                                                | 24.4 ms: 1.05x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.63 ms: 1.05x faster                                  |
| telco                   | 6.58 ms                                                | 6.31 ms: 1.04x faster                                  |
| logging_simple          | 6.03 us                                                | 5.78 us: 1.04x faster                                  |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| logging_format          | 6.68 us                                                | 6.41 us: 1.04x faster                                  |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                   |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                   |
| fannkuch                | 388 ms                                                 | 373 ms: 1.04x faster                                   |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 65.6 ms: 1.04x faster                                  |
| mako                    | 10.1 ms                                                | 9.72 ms: 1.04x faster                                  |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                   |
| tornado_http            | 96.3 ms                                                | 93.1 ms: 1.03x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                  |
| nqueens                 | 83.4 ms                                                | 80.7 ms: 1.03x faster                                  |
| scimark_fft             | 328 ms                                                 | 318 ms: 1.03x faster                                   |
| dulwich_log             | 63.7 ms                                                | 61.6 ms: 1.03x faster                                  |
| mdp                     | 2.62 sec                                               | 2.54 sec: 1.03x faster                                 |
| sqlglot_optimize        | 53.1 ms                                                | 51.5 ms: 1.03x faster                                  |
| coverage                | 100 ms                                                 | 97.3 ms: 1.03x faster                                  |
| thrift                  | 756 us                                                 | 736 us: 1.03x faster                                   |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                   |
| chaos                   | 69.2 ms                                                | 67.4 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.03x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.22 ms: 1.02x faster                                  |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                   |
| genshi_text             | 21.6 ms                                                | 21.1 ms: 1.02x faster                                  |
| django_template         | 32.6 ms                                                | 32.0 ms: 1.02x faster                                  |
| python_startup          | 8.52 ms                                                | 8.37 ms: 1.02x faster                                  |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| chameleon               | 6.47 ms                                                | 6.37 ms: 1.02x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 53.1 ms: 1.01x faster                                  |
| generators              | 73.5 ms                                                | 72.6 ms: 1.01x faster                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.91 us: 1.01x faster                                  |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.08 ms: 1.01x slower                                  |
| pickle_list             | 4.11 us                                                | 4.16 us: 1.01x slower                                  |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.02x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 638 ms: 1.02x slower                                   |
| async_tree_none         | 526 ms                                                 | 536 ms: 1.02x slower                                   |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                 |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                   |
| pickle                  | 10.1 us                                                | 10.4 us: 1.04x slower                                  |
| regex_v8                | 22.0 ms                                                | 22.9 ms: 1.04x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.64 us: 1.05x slower                                  |
| nbody                   | 93.1 ms                                                | 98.1 ms: 1.05x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 46.0 ns: 1.07x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (5): pylint, async_tree_cpu_io_mixed, xml_etree_generate, crypto_pyaes, scimark_lu
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221029-3.12.0a2+-fc94d55/bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x


# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 827b81b
- commit date: 2023-02-09
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                              |
| html5lib       | 63.2 ms                                                | 61.4 ms: 1.03x faster                                               |
| tornado_http   | 96.6 ms                                                | 93.9 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 73.0 ms: 1.05x faster                                               |
| pidigits       | 199 ms                                                 | 191 ms: 1.05x faster                                                |
| nbody          | 95.0 ms                                                | 94.5 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| regex_v8       | 22.3 ms                                                | 21.4 ms: 1.04x faster                                               |
| regex_effbot   | 3.36 ms                                                | 3.46 ms: 1.03x slower                                               |
| regex_dna      | 203 ms                                                 | 218 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.58 ms: 1.32x faster                                               |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_pure_python   | 304 us                                                 | 289 us: 1.05x faster                                                |
| unpickle_list        | 4.95 us                                                | 4.88 us: 1.01x faster                                               |
| pickle_dict          | 31.4 us                                                | 31.2 us: 1.01x faster                                               |
| pickle_list          | 4.17 us                                                | 4.21 us: 1.01x slower                                               |
| xml_etree_process    | 53.8 ms                                                | 54.9 ms: 1.02x slower                                               |
| pickle               | 9.79 us                                                | 10.1 us: 1.04x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 80.4 ms: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.93 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.47 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.1 ms: 1.11x faster                                               |
| genshi_text     | 22.1 ms                                                | 21.0 ms: 1.06x faster                                               |
| mako            | 9.85 ms                                                | 9.73 ms: 1.01x faster                                               |
| django_template | 32.5 ms                                                | 33.6 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.58 ms: 1.32x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                |
| deltablue               | 3.64 ms                                                | 3.22 ms: 1.13x faster                                               |
| genshi_xml              | 52.1 ms                                                | 47.1 ms: 1.11x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.99 ms: 1.10x faster                                               |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                               |
| nqueens                 | 85.0 ms                                                | 78.1 ms: 1.09x faster                                               |
| scimark_fft             | 329 ms                                                 | 302 ms: 1.09x faster                                                |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.08x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| json                    | 4.95 ms                                                | 4.64 ms: 1.07x faster                                               |
| fannkuch                | 388 ms                                                 | 364 ms: 1.07x faster                                                |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| richards                | 46.2 ms                                                | 43.3 ms: 1.07x faster                                               |
| deepcopy_memo           | 36.4 us                                                | 34.2 us: 1.06x faster                                               |
| hexiom                  | 6.35 ms                                                | 5.97 ms: 1.06x faster                                               |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                |
| logging_silent          | 98.5 ns                                                | 93.2 ns: 1.06x faster                                               |
| logging_simple          | 6.06 us                                                | 5.74 us: 1.06x faster                                               |
| genshi_text             | 22.1 ms                                                | 21.0 ms: 1.06x faster                                               |
| mdp                     | 2.62 sec                                               | 2.49 sec: 1.05x faster                                              |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                               |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                                |
| pickle_pure_python      | 304 us                                                 | 289 us: 1.05x faster                                                |
| chaos                   | 68.6 ms                                                | 65.6 ms: 1.05x faster                                               |
| float                   | 76.3 ms                                                | 73.0 ms: 1.05x faster                                               |
| pidigits                | 199 ms                                                 | 191 ms: 1.05x faster                                                |
| deepcopy                | 344 us                                                 | 329 us: 1.05x faster                                                |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                               |
| regex_v8                | 22.3 ms                                                | 21.4 ms: 1.04x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| logging_format          | 6.62 us                                                | 6.36 us: 1.04x faster                                               |
| scimark_monte_carlo     | 68.3 ms                                                | 65.9 ms: 1.04x faster                                               |
| bench_thread_pool       | 810 us                                                 | 785 us: 1.03x faster                                                |
| tornado_http            | 96.6 ms                                                | 93.9 ms: 1.03x faster                                               |
| html5lib                | 63.2 ms                                                | 61.4 ms: 1.03x faster                                               |
| sympy_expand            | 472 ms                                                 | 459 ms: 1.03x faster                                                |
| unpack_sequence         | 43.4 ns                                                | 42.3 ns: 1.03x faster                                               |
| coverage                | 101 ms                                                 | 97.9 ms: 1.03x faster                                               |
| dulwich_log             | 63.9 ms                                                | 62.4 ms: 1.02x faster                                               |
| pyflate                 | 417 ms                                                 | 407 ms: 1.02x faster                                                |
| sqlglot_optimize        | 53.0 ms                                                | 51.7 ms: 1.02x faster                                               |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                              |
| coroutines              | 26.1 ms                                                | 25.5 ms: 1.02x faster                                               |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| telco                   | 6.62 ms                                                | 6.49 ms: 1.02x faster                                               |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                               |
| deepcopy_reduce         | 2.97 us                                                | 2.92 us: 1.02x faster                                               |
| raytrace                | 290 ms                                                 | 286 ms: 1.02x faster                                                |
| spectral_norm           | 99.9 ms                                                | 98.5 ms: 1.01x faster                                               |
| unpickle_list           | 4.95 us                                                | 4.88 us: 1.01x faster                                               |
| sqlalchemy_declarative  | 139 ms                                                 | 137 ms: 1.01x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                |
| pprint_pformat          | 1.44 sec                                               | 1.42 sec: 1.01x faster                                              |
| sqlalchemy_imperative   | 18.0 ms                                                | 17.8 ms: 1.01x faster                                               |
| mako                    | 9.85 ms                                                | 9.73 ms: 1.01x faster                                               |
| pickle_dict             | 31.4 us                                                | 31.2 us: 1.01x faster                                               |
| nbody                   | 95.0 ms                                                | 94.5 ms: 1.01x faster                                               |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                              |
| pickle_list             | 4.17 us                                                | 4.21 us: 1.01x slower                                               |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.01x slower                                                |
| pprint_safe_repr        | 691 ms                                                 | 699 ms: 1.01x slower                                                |
| xml_etree_process       | 53.8 ms                                                | 54.9 ms: 1.02x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.46 ms: 1.03x slower                                               |
| pickle                  | 9.79 us                                                | 10.1 us: 1.04x slower                                               |
| django_template         | 32.5 ms                                                | 33.6 ms: 1.04x slower                                               |
| scimark_lu              | 107 ms                                                 | 111 ms: 1.04x slower                                                |
| async_tree_memoization  | 625 ms                                                 | 649 ms: 1.04x slower                                                |
| sqlglot_transpile       | 1.66 ms                                                | 1.73 ms: 1.04x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.43 ms: 1.04x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.61 us: 1.05x slower                                               |
| crypto_pyaes            | 73.9 ms                                                | 77.7 ms: 1.05x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 80.4 ms: 1.06x slower                                               |
| python_startup          | 8.36 ms                                                | 8.93 ms: 1.07x slower                                               |
| regex_dna               | 203 ms                                                 | 218 ms: 1.07x slower                                                |
| generators              | 72.2 ms                                                | 77.7 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.47 ms: 1.08x slower                                               |
| async_generators        | 359 ms                                                 | 424 ms: 1.18x slower                                                |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (7): unpickle, async_tree_none, chameleon, bench_mp_pool, xml_etree_iterparse, async_tree_cpu_io_mixed, thrift
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230209-3.12.0a5+-827b81b/bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2

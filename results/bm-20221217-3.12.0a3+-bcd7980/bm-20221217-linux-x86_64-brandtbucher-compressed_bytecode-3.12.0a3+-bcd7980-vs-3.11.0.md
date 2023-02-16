
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compressed_bytecode
- machine: linux-x86_64
- commit hash: bcd7980
- commit date: 2022-12-17
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                        |
| chameleon      | 6.38 ms                                                | 6.43 ms: 1.01x slower                                                       |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                      |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.3 ms: 1.06x faster                                                       |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| nbody          | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                        |
| regex_v8       | 22.2 ms                                                | 22.2 ms: 1.00x faster                                                       |
| regex_effbot   | 3.46 ms                                                | 3.58 ms: 1.04x slower                                                       |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.49 ms: 1.30x faster                                                       |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                                        |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                        |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| pickle_list          | 4.14 us                                                | 4.12 us: 1.01x faster                                                       |
| xml_etree_generate   | 75.9 ms                                                | 77.2 ms: 1.02x slower                                                       |
| unpickle_list        | 4.99 us                                                | 5.12 us: 1.03x slower                                                       |
| pickle               | 9.90 us                                                | 10.2 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.50 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.04 ms                                                | 6.08 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                       |
| mako            | 9.83 ms                                                | 9.72 ms: 1.01x faster                                                       |
| genshi_text     | 21.5 ms                                                | 21.3 ms: 1.01x faster                                                       |
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.49 ms: 1.30x faster                                                       |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                        |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.03 ms: 1.14x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.22 ms: 1.14x faster                                                       |
| richards                | 46.1 ms                                                | 41.6 ms: 1.11x faster                                                       |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                       |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                                        |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                       |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.08x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 33.5 us: 1.07x faster                                                       |
| unpack_sequence         | 44.5 ns                                                | 41.6 ns: 1.07x faster                                                       |
| nqueens                 | 83.8 ms                                                | 78.5 ms: 1.07x faster                                                       |
| logging_silent          | 98.0 ns                                                | 92.1 ns: 1.06x faster                                                       |
| float                   | 76.8 ms                                                | 72.3 ms: 1.06x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.69 us: 1.06x faster                                                       |
| sympy_expand            | 475 ms                                                 | 449 ms: 1.06x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 774 us: 1.05x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.13 sec: 1.05x faster                                                      |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                        |
| coroutines              | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.88 us: 1.05x faster                                                       |
| deepcopy                | 341 us                                                 | 326 us: 1.05x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                      |
| sqlglot_optimize        | 52.7 ms                                                | 50.5 ms: 1.04x faster                                                       |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                      |
| hexiom                  | 6.34 ms                                                | 6.08 ms: 1.04x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 677 ms: 1.04x faster                                                        |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                        |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| telco                   | 6.43 ms                                                | 6.17 ms: 1.04x faster                                                       |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                       |
| chaos                   | 68.7 ms                                                | 66.1 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                        |
| mdp                     | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                      |
| fannkuch                | 384 ms                                                 | 372 ms: 1.03x faster                                                        |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                        |
| scimark_fft             | 325 ms                                                 | 315 ms: 1.03x faster                                                        |
| logging_format          | 6.48 us                                                | 6.28 us: 1.03x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.0 ms: 1.03x faster                                                       |
| sympy_sum               | 166 ms                                                 | 161 ms: 1.03x faster                                                        |
| pyflate                 | 419 ms                                                 | 407 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 66.1 ms: 1.03x faster                                                       |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                       |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 74.1 ms: 1.02x faster                                                       |
| spectral_norm           | 98.1 ms                                                | 96.1 ms: 1.02x faster                                                       |
| thrift                  | 760 us                                                 | 745 us: 1.02x faster                                                        |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| json                    | 4.87 ms                                                | 4.80 ms: 1.01x faster                                                       |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.01x faster                                                        |
| mako                    | 9.83 ms                                                | 9.72 ms: 1.01x faster                                                       |
| genshi_text             | 21.5 ms                                                | 21.3 ms: 1.01x faster                                                       |
| python_startup          | 8.58 ms                                                | 8.50 ms: 1.01x faster                                                       |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                        |
| pickle_list             | 4.14 us                                                | 4.12 us: 1.01x faster                                                       |
| regex_v8                | 22.2 ms                                                | 22.2 ms: 1.00x faster                                                       |
| chameleon               | 6.38 ms                                                | 6.43 ms: 1.01x slower                                                       |
| python_startup_no_site  | 6.04 ms                                                | 6.08 ms: 1.01x slower                                                       |
| async_tree_none         | 526 ms                                                 | 533 ms: 1.01x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| xml_etree_generate      | 75.9 ms                                                | 77.2 ms: 1.02x slower                                                       |
| django_template         | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                       |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.02x slower                                                       |
| sqlglot_parse           | 1.36 ms                                                | 1.39 ms: 1.02x slower                                                       |
| unpickle_list           | 4.99 us                                                | 5.12 us: 1.03x slower                                                       |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                                       |
| pickle                  | 9.90 us                                                | 10.2 us: 1.04x slower                                                       |
| regex_effbot            | 3.46 ms                                                | 3.58 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed | 736 ms                                                 | 765 ms: 1.04x slower                                                        |
| nbody                   | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                       |
| generators              | 73.5 ms                                                | 77.6 ms: 1.06x slower                                                       |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (7): async_generators, xml_etree_process, bench_mp_pool, coverage, djangocms, unpickle, async_tree_memoization
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221217-3.12.0a3+-bcd7980/bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980.json: mypy

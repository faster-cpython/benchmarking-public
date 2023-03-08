
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_dict_global_
- machine: linux-x86_64
- commit hash: f707a1b
- commit date: 2023-02-28
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                              |
| chameleon      | 6.38 ms                                                | 6.28 ms: 1.02x faster                                                             |
| docutils       | 2.60 sec                                               | 2.57 sec: 1.01x faster                                                            |
| html5lib       | 64.8 ms                                                | 61.7 ms: 1.05x faster                                                             |
| tornado_http   | 96.5 ms                                                | 95.5 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                              |
| float          | 76.8 ms                                                | 74.3 ms: 1.03x faster                                                             |
| nbody          | 90.0 ms                                                | 93.9 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 133 ms: 1.02x faster                                                              |
| regex_v8       | 22.2 ms                                                | 21.9 ms: 1.02x faster                                                             |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                              |
| regex_effbot   | 3.46 ms                                                | 3.63 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.55 ms: 1.29x faster                                                             |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                              |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                                              |
| json_loads           | 26.1 us                                                | 24.3 us: 1.07x faster                                                             |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.07x faster                                                              |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                                             |
| pickle_list          | 4.14 us                                                | 4.09 us: 1.01x faster                                                             |
| unpickle_list        | 4.99 us                                                | 4.96 us: 1.01x faster                                                             |
| unpickle             | 13.3 us                                                | 13.6 us: 1.03x slower                                                             |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                             |
| xml_etree_process    | 53.7 ms                                                | 55.6 ms: 1.04x slower                                                             |
| xml_etree_generate   | 75.9 ms                                                | 80.8 ms: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.06 ms: 1.06x slower                                                             |
| python_startup_no_site | 6.04 ms                                                | 6.57 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.6 ms: 1.06x faster                                                             |
| django_template | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                                             |
| asyncio_tcp             | 883 ms                                                 | 503 ms: 1.75x faster                                                              |
| json_dumps              | 12.4 ms                                                | 9.55 ms: 1.29x faster                                                             |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                              |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                              |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                             |
| coroutines              | 26.2 ms                                                | 23.5 ms: 1.11x faster                                                             |
| mdp                     | 2.63 sec                                               | 2.40 sec: 1.10x faster                                                            |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                                              |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                              |
| json_loads              | 26.1 us                                                | 24.3 us: 1.07x faster                                                             |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.07x faster                                                              |
| richards                | 46.1 ms                                                | 43.2 ms: 1.07x faster                                                             |
| coverage                | 99.3 ms                                                | 93.1 ms: 1.07x faster                                                             |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                            |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                                              |
| genshi_xml              | 51.4 ms                                                | 48.6 ms: 1.06x faster                                                             |
| json                    | 4.87 ms                                                | 4.62 ms: 1.05x faster                                                             |
| html5lib                | 64.8 ms                                                | 61.7 ms: 1.05x faster                                                             |
| deepcopy_memo           | 35.8 us                                                | 34.1 us: 1.05x faster                                                             |
| spectral_norm           | 98.1 ms                                                | 93.8 ms: 1.05x faster                                                             |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                              |
| logging_simple          | 6.02 us                                                | 5.78 us: 1.04x faster                                                             |
| nqueens                 | 83.8 ms                                                | 80.5 ms: 1.04x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                            |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                              |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                              |
| pprint_safe_repr        | 706 ms                                                 | 679 ms: 1.04x faster                                                              |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                             |
| logging_silent          | 98.0 ns                                                | 94.5 ns: 1.04x faster                                                             |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.42 ms: 1.04x faster                                                             |
| float                   | 76.8 ms                                                | 74.3 ms: 1.03x faster                                                             |
| logging_format          | 6.48 us                                                | 6.27 us: 1.03x faster                                                             |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                                              |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                             |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                              |
| crypto_pyaes            | 75.7 ms                                                | 73.6 ms: 1.03x faster                                                             |
| hexiom                  | 6.34 ms                                                | 6.16 ms: 1.03x faster                                                             |
| regex_compile           | 136 ms                                                 | 133 ms: 1.02x faster                                                              |
| bench_thread_pool       | 817 us                                                 | 797 us: 1.02x faster                                                              |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                             |
| sqlglot_optimize        | 52.7 ms                                                | 51.6 ms: 1.02x faster                                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 66.6 ms: 1.02x faster                                                             |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                                              |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                              |
| chameleon               | 6.38 ms                                                | 6.28 ms: 1.02x faster                                                             |
| regex_v8                | 22.2 ms                                                | 21.9 ms: 1.02x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                                            |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.50 ms: 1.01x faster                                                             |
| pickle_list             | 4.14 us                                                | 4.09 us: 1.01x faster                                                             |
| docutils                | 2.60 sec                                               | 2.57 sec: 1.01x faster                                                            |
| tornado_http            | 96.5 ms                                                | 95.5 ms: 1.01x faster                                                             |
| raytrace                | 291 ms                                                 | 289 ms: 1.01x faster                                                              |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                              |
| sympy_integrate         | 21.0 ms                                                | 20.8 ms: 1.01x faster                                                             |
| sympy_str               | 291 ms                                                 | 289 ms: 1.01x faster                                                              |
| unpickle_list           | 4.99 us                                                | 4.96 us: 1.01x faster                                                             |
| pyflate                 | 419 ms                                                 | 417 ms: 1.00x faster                                                              |
| dulwich_log             | 64.0 ms                                                | 63.8 ms: 1.00x faster                                                             |
| gc_traversal            | 3.82 ms                                                | 3.83 ms: 1.00x slower                                                             |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.02x slower                                                              |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                              |
| django_template         | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                             |
| unpickle                | 13.3 us                                                | 13.6 us: 1.03x slower                                                             |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                             |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                              |
| xml_etree_process       | 53.7 ms                                                | 55.6 ms: 1.04x slower                                                             |
| async_tree_memoization  | 624 ms                                                 | 650 ms: 1.04x slower                                                              |
| nbody                   | 90.0 ms                                                | 93.9 ms: 1.04x slower                                                             |
| thrift                  | 760 us                                                 | 793 us: 1.04x slower                                                              |
| regex_effbot            | 3.46 ms                                                | 3.63 ms: 1.05x slower                                                             |
| python_startup          | 8.58 ms                                                | 9.06 ms: 1.06x slower                                                             |
| sqlglot_transpile       | 1.65 ms                                                | 1.75 ms: 1.06x slower                                                             |
| sqlite_synth            | 2.48 us                                                | 2.63 us: 1.06x slower                                                             |
| xml_etree_generate      | 75.9 ms                                                | 80.8 ms: 1.07x slower                                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.46 ms: 1.07x slower                                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.57 ms: 1.09x slower                                                             |
| async_generators        | 356 ms                                                 | 417 ms: 1.17x slower                                                              |
| dask                    | 365 ms                                                 | 510 ms: 1.40x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (12): async_tree_none, genshi_text, unpack_sequence, telco, chaos, mako, bench_mp_pool, async_tree_cpu_io_mixed, djangocms, xml_etree_iterparse, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-f707a1b/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b.json: comprehensions

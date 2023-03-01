
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: 969caba
- commit date: 2023-02-28
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                              |
| chameleon      | 6.38 ms                                                | 6.33 ms: 1.01x faster                                                             |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                            |
| html5lib       | 64.8 ms                                                | 61.9 ms: 1.05x faster                                                             |
| tornado_http   | 96.5 ms                                                | 95.3 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                              |
| float          | 76.8 ms                                                | 73.8 ms: 1.04x faster                                                             |
| nbody          | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 133 ms: 1.02x faster                                                              |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                             |
| regex_dna      | 203 ms                                                 | 200 ms: 1.02x faster                                                              |
| regex_effbot   | 3.46 ms                                                | 3.55 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.61 ms: 1.29x faster                                                             |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                              |
| json_loads           | 26.1 us                                                | 23.8 us: 1.09x faster                                                             |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                              |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 99.1 ms: 1.05x faster                                                             |
| pickle_dict          | 31.2 us                                                | 29.7 us: 1.05x faster                                                             |
| pickle_list          | 4.14 us                                                | 4.01 us: 1.03x faster                                                             |
| unpickle_list        | 4.99 us                                                | 4.91 us: 1.02x faster                                                             |
| pickle               | 9.90 us                                                | 9.95 us: 1.01x slower                                                             |
| xml_etree_process    | 53.7 ms                                                | 55.6 ms: 1.04x slower                                                             |
| xml_etree_generate   | 75.9 ms                                                | 80.7 ms: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.03 ms: 1.05x slower                                                             |
| python_startup_no_site | 6.04 ms                                                | 6.55 ms: 1.08x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.2 ms: 1.07x faster                                                             |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                             |
| mako            | 9.83 ms                                                | 10.2 ms: 1.03x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.7 ms: 2.39x faster                                                             |
| asyncio_tcp             | 883 ms                                                 | 498 ms: 1.77x faster                                                              |
| json_dumps              | 12.4 ms                                                | 9.61 ms: 1.29x faster                                                             |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                              |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                              |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                                             |
| coroutines              | 26.2 ms                                                | 23.1 ms: 1.13x faster                                                             |
| mdp                     | 2.63 sec                                               | 2.38 sec: 1.10x faster                                                            |
| json_loads              | 26.1 us                                                | 23.8 us: 1.09x faster                                                             |
| richards                | 46.1 ms                                                | 42.2 ms: 1.09x faster                                                             |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                                            |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                              |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                                              |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                              |
| genshi_xml              | 51.4 ms                                                | 48.2 ms: 1.07x faster                                                             |
| json                    | 4.87 ms                                                | 4.59 ms: 1.06x faster                                                             |
| coverage                | 99.3 ms                                                | 93.7 ms: 1.06x faster                                                             |
| logging_silent          | 98.0 ns                                                | 92.6 ns: 1.06x faster                                                             |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                              |
| deepcopy_memo           | 35.8 us                                                | 34.1 us: 1.05x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 99.1 ms: 1.05x faster                                                             |
| pickle_dict             | 31.2 us                                                | 29.7 us: 1.05x faster                                                             |
| pyflate                 | 419 ms                                                 | 400 ms: 1.05x faster                                                              |
| html5lib                | 64.8 ms                                                | 61.9 ms: 1.05x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                              |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                                             |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                              |
| float                   | 76.8 ms                                                | 73.8 ms: 1.04x faster                                                             |
| fannkuch                | 384 ms                                                 | 370 ms: 1.04x faster                                                              |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                             |
| hexiom                  | 6.34 ms                                                | 6.11 ms: 1.04x faster                                                             |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                              |
| deepcopy                | 341 us                                                 | 330 us: 1.04x faster                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                                            |
| chaos                   | 68.7 ms                                                | 66.3 ms: 1.04x faster                                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.03x faster                                                             |
| pickle_list             | 4.14 us                                                | 4.01 us: 1.03x faster                                                             |
| pprint_safe_repr        | 706 ms                                                 | 687 ms: 1.03x faster                                                              |
| deepcopy_reduce         | 3.02 us                                                | 2.94 us: 1.03x faster                                                             |
| bench_thread_pool       | 817 us                                                 | 796 us: 1.03x faster                                                              |
| logging_simple          | 6.02 us                                                | 5.87 us: 1.03x faster                                                             |
| sympy_expand            | 475 ms                                                 | 464 ms: 1.02x faster                                                              |
| spectral_norm           | 98.1 ms                                                | 95.8 ms: 1.02x faster                                                             |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.02x faster                                                             |
| scimark_fft             | 325 ms                                                 | 318 ms: 1.02x faster                                                              |
| regex_compile           | 136 ms                                                 | 133 ms: 1.02x faster                                                              |
| raytrace                | 291 ms                                                 | 285 ms: 1.02x faster                                                              |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                            |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 66.7 ms: 1.02x faster                                                             |
| regex_dna               | 203 ms                                                 | 200 ms: 1.02x faster                                                              |
| unpickle_list           | 4.99 us                                                | 4.91 us: 1.02x faster                                                             |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                                             |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                              |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                             |
| async_tree_none         | 526 ms                                                 | 519 ms: 1.01x faster                                                              |
| sympy_str               | 291 ms                                                 | 287 ms: 1.01x faster                                                              |
| tornado_http            | 96.5 ms                                                | 95.3 ms: 1.01x faster                                                             |
| nqueens                 | 83.8 ms                                                | 82.8 ms: 1.01x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                            |
| logging_format          | 6.48 us                                                | 6.41 us: 1.01x faster                                                             |
| crypto_pyaes            | 75.7 ms                                                | 75.1 ms: 1.01x faster                                                             |
| chameleon               | 6.38 ms                                                | 6.33 ms: 1.01x faster                                                             |
| unpack_sequence         | 44.5 ns                                                | 44.3 ns: 1.00x faster                                                             |
| dulwich_log             | 64.0 ms                                                | 64.2 ms: 1.00x slower                                                             |
| gc_traversal            | 3.82 ms                                                | 3.83 ms: 1.00x slower                                                             |
| pickle                  | 9.90 us                                                | 9.95 us: 1.01x slower                                                             |
| sympy_sum               | 166 ms                                                 | 169 ms: 1.02x slower                                                              |
| thrift                  | 760 us                                                 | 775 us: 1.02x slower                                                              |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                             |
| regex_effbot            | 3.46 ms                                                | 3.55 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.73 ms: 1.03x slower                                                             |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                              |
| mako                    | 9.83 ms                                                | 10.2 ms: 1.03x slower                                                             |
| xml_etree_process       | 53.7 ms                                                | 55.6 ms: 1.04x slower                                                             |
| nbody                   | 90.0 ms                                                | 93.6 ms: 1.04x slower                                                             |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                                             |
| python_startup          | 8.58 ms                                                | 9.03 ms: 1.05x slower                                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                             |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                             |
| xml_etree_generate      | 75.9 ms                                                | 80.7 ms: 1.06x slower                                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.55 ms: 1.08x slower                                                             |
| async_generators        | 356 ms                                                 | 418 ms: 1.17x slower                                                              |
| dask                    | 365 ms                                                 | 506 ms: 1.39x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (9): sqlalchemy_declarative, genshi_text, bench_mp_pool, async_tree_cpu_io_mixed, unpickle, telco, sqlalchemy_imperative, djangocms, async_tree_memoization
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-969caba/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba.json: comprehensions

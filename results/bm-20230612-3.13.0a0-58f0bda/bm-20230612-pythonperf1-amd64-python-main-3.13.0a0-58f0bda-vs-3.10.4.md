
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 58f0bda
- commit date: 2023-06-12
- overall geometric mean: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.68 sec: 1.12x faster                                     |
| tornado_http   | 109 ms                                                      | 102 ms: 1.07x faster                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.9 ms: 1.06x faster                                      |
| pidigits       | 145 ms                                                      | 153 ms: 1.05x slower                                       |
| nbody          | 69.3 ms                                                     | 77.8 ms: 1.12x slower                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 89.9 ms: 1.15x faster                                      |
| regex_dna      | 132 ms                                                      | 122 ms: 1.08x faster                                       |
| regex_v8       | 15.0 ms                                                     | 14.2 ms: 1.06x faster                                      |
| regex_effbot   | 1.66 ms                                                     | 1.64 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.76 ms: 1.48x faster                                      |
| pickle_pure_python   | 257 us                                                      | 202 us: 1.27x faster                                       |
| unpickle_pure_python | 171 us                                                      | 143 us: 1.20x faster                                       |
| tomli_loads          | 1.62 sec                                                    | 1.48 sec: 1.10x faster                                     |
| xml_etree_process    | 43.4 ms                                                     | 40.1 ms: 1.08x faster                                      |
| unpickle             | 9.17 us                                                     | 8.49 us: 1.08x faster                                      |
| xml_etree_parse      | 102 ms                                                      | 94.5 ms: 1.08x faster                                      |
| json_loads           | 14.2 us                                                     | 13.9 us: 1.02x faster                                      |
| unpickle_list        | 2.81 us                                                     | 2.89 us: 1.03x slower                                      |
| pickle               | 6.80 us                                                     | 7.14 us: 1.05x slower                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 67.1 ms: 1.06x slower                                      |
| xml_etree_generate   | 54.5 ms                                                     | 58.0 ms: 1.06x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.4 us: 1.09x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.93 us: 1.13x slower                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 20.7 ms: 1.03x slower                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.56 ms: 1.16x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.5 us: 3.40x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.18 ms: 1.92x faster                                      |
| richards_super           | 51.7 ms                                                     | 30.5 ms: 1.69x faster                                      |
| mypy2                    | 352 ms                                                      | 222 ms: 1.59x faster                                       |
| logging_silent           | 96.4 ns                                                     | 62.9 ns: 1.53x faster                                      |
| richards                 | 41.2 ms                                                     | 27.1 ms: 1.52x faster                                      |
| go                       | 136 ms                                                      | 91.9 ms: 1.48x faster                                      |
| json_dumps               | 8.50 ms                                                     | 5.76 ms: 1.48x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 848 us: 1.44x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 60.5 ms: 1.41x faster                                      |
| raytrace                 | 271 ms                                                      | 197 ms: 1.38x faster                                       |
| sqlglot_transpile        | 1.46 ms                                                     | 1.07 ms: 1.37x faster                                      |
| async_tree_io            | 1.07 sec                                                    | 778 ms: 1.37x faster                                       |
| generators               | 31.6 ms                                                     | 23.2 ms: 1.36x faster                                      |
| async_tree_memoization   | 497 ms                                                      | 368 ms: 1.35x faster                                       |
| async_tree_none          | 420 ms                                                      | 315 ms: 1.34x faster                                       |
| chaos                    | 58.9 ms                                                     | 44.6 ms: 1.32x faster                                      |
| hexiom                   | 5.52 ms                                                     | 4.22 ms: 1.31x faster                                      |
| crypto_pyaes             | 62.3 ms                                                     | 48.4 ms: 1.29x faster                                      |
| pickle_pure_python       | 257 us                                                      | 202 us: 1.27x faster                                       |
| scimark_sor              | 105 ms                                                      | 82.9 ms: 1.27x faster                                      |
| pyflate                  | 387 ms                                                      | 313 ms: 1.23x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 143 us: 1.20x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 46.7 ms: 1.19x faster                                      |
| spectral_norm            | 78.0 ms                                                     | 65.6 ms: 1.19x faster                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 513 ms: 1.19x faster                                       |
| pycparser                | 868 ms                                                      | 734 ms: 1.18x faster                                       |
| mako                     | 8.80 ms                                                     | 7.56 ms: 1.16x faster                                      |
| deepcopy_memo            | 28.5 us                                                     | 24.6 us: 1.16x faster                                      |
| regex_compile            | 103 ms                                                      | 89.9 ms: 1.15x faster                                      |
| mdp                      | 1.71 sec                                                    | 1.51 sec: 1.14x faster                                     |
| sqlglot_optimize         | 39.0 ms                                                     | 34.5 ms: 1.13x faster                                      |
| docutils                 | 1.89 sec                                                    | 1.68 sec: 1.12x faster                                     |
| pprint_safe_repr         | 589 ms                                                      | 533 ms: 1.10x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 184 ms: 1.10x faster                                       |
| comprehensions           | 16.0 us                                                     | 14.5 us: 1.10x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.10 sec: 1.10x faster                                     |
| tomli_loads              | 1.62 sec                                                    | 1.48 sec: 1.10x faster                                     |
| xml_etree_process        | 43.4 ms                                                     | 40.1 ms: 1.08x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.49 us: 1.08x faster                                      |
| regex_dna                | 132 ms                                                      | 122 ms: 1.08x faster                                       |
| xml_etree_parse          | 102 ms                                                      | 94.5 ms: 1.08x faster                                      |
| tornado_http             | 109 ms                                                      | 102 ms: 1.07x faster                                       |
| nqueens                  | 67.0 ms                                                     | 62.9 ms: 1.07x faster                                      |
| regex_v8                 | 15.0 ms                                                     | 14.2 ms: 1.06x faster                                      |
| asyncio_tcp              | 712 ms                                                      | 672 ms: 1.06x faster                                       |
| float                    | 60.2 ms                                                     | 56.9 ms: 1.06x faster                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.52 ms: 1.06x faster                                      |
| sqlite_synth             | 1.84 us                                                     | 1.75 us: 1.05x faster                                      |
| coroutines               | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                      |
| deepcopy                 | 255 us                                                      | 244 us: 1.05x faster                                       |
| scimark_fft              | 193 ms                                                      | 186 ms: 1.04x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 45.8 ms: 1.04x faster                                      |
| bench_thread_pool        | 946 us                                                      | 910 us: 1.04x faster                                       |
| create_gc_cycles         | 782 us                                                      | 755 us: 1.04x faster                                       |
| json                     | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                      |
| json_loads               | 14.2 us                                                     | 13.9 us: 1.02x faster                                      |
| regex_effbot             | 1.66 ms                                                     | 1.64 ms: 1.02x faster                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.19 us: 1.02x slower                                      |
| unpickle_list            | 2.81 us                                                     | 2.89 us: 1.03x slower                                      |
| python_startup           | 20.0 ms                                                     | 20.7 ms: 1.03x slower                                      |
| fannkuch                 | 258 ms                                                      | 267 ms: 1.03x slower                                       |
| pickle                   | 6.80 us                                                     | 7.14 us: 1.05x slower                                      |
| pidigits                 | 145 ms                                                      | 153 ms: 1.05x slower                                       |
| meteor_contest           | 72.5 ms                                                     | 76.5 ms: 1.05x slower                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 67.1 ms: 1.06x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 58.0 ms: 1.06x slower                                      |
| logging_simple           | 6.20 us                                                     | 6.67 us: 1.08x slower                                      |
| logging_format           | 6.66 us                                                     | 7.18 us: 1.08x slower                                      |
| unpack_sequence          | 37.8 ns                                                     | 40.9 ns: 1.08x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.4 us: 1.09x slower                                      |
| telco                    | 3.78 ms                                                     | 4.18 ms: 1.11x slower                                      |
| async_generators         | 224 ms                                                      | 248 ms: 1.11x slower                                       |
| nbody                    | 69.3 ms                                                     | 77.8 ms: 1.12x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                      |
| pathlib                  | 77.4 ms                                                     | 86.9 ms: 1.12x slower                                      |
| pickle_list              | 2.59 us                                                     | 2.93 us: 1.13x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 69.2 ms: 1.14x slower                                      |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 2.33 sec: 1.15x slower                                     |
| gc_traversal             | 1.34 ms                                                     | 1.55 ms: 1.16x slower                                      |
| coverage                 | 40.0 ms                                                     | 54.7 ms: 1.37x slower                                      |
| Geometric mean           | (ref)                                                       | 1.13x faster                                               |
Ignored benchmarks (17) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
